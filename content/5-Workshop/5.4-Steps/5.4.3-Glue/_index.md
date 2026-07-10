---
title: "Step 3: AWS Glue ETL"
date: 2024-01-01
weight: 3
chapter: false
pre: " <b> 5.4.3 </b> "
---

# Step 3: AWS Glue ETL Jobs

In this step, you will create the Glue Data Catalog database and three ETL jobs that process data through the Medallion tiers: Raw → Bronze → Silver → Gold.

**Estimated time:** 30–40 minutes

---

## 3.1 Create Glue Data Catalog Database

**AWS Console → AWS Glue → Data Catalog → Databases → Add database**

| Field | Value |
|-------|-------|
| Database name | `customer_behavior_catalog_db` |
| Description | `Catalog for Customer Behavior Lakehouse Gold tables` |
| Location (optional) | `s3://customer-behavior-lakehouse1/gold/` |

Click **Create database**.

> 📌 **[INSERT SCREENSHOT: Glue Database created]**
> `![Glue Database](/result/AWS Glue/Glue Database.jpg)`

---

## 3.2 Upload ETL Scripts to S3

Before creating Glue jobs, upload the Python scripts to an S3 path that Glue can access:

```bash
# Create a scripts prefix in S3
aws s3 cp raw_to_bronze_job.py s3://customer-behavior-lakehouse1/scripts/raw_to_bronze_job.py
aws s3 cp bronze_to_silver_job.py s3://customer-behavior-lakehouse1/scripts/bronze_to_silver_job.py
aws s3 cp silver_to_gold_job.py s3://customer-behavior-lakehouse1/scripts/silver_to_gold_job.py

# Verify
aws s3 ls s3://customer-behavior-lakehouse1/scripts/
```

---

## 3.3 Create Glue ETL Job 1: Raw → Bronze

**AWS Console → AWS Glue → ETL Jobs → Create job → Script editor**

Select **Spark** as the engine, then paste the content of `raw_to_bronze_job.py`.

**Job properties:**

| Field | Value |
|-------|-------|
| Name | `raw-to-bronze-job` |
| IAM Role | `AWSGlueServiceRole-lakehouse` |
| Glue version | Glue 4.0 |
| Language | Python 3 |
| Worker type | G.1X |
| Number of workers | 2 |
| Job timeout | 30 minutes |
| Script path | `s3://customer-behavior-lakehouse1/scripts/raw_to_bronze_job.py` |
| Temporary path | `s3://customer-behavior-lakehouse1/tmp/` |

**Job script (`raw_to_bronze_job.py`) key logic:**

```python
BUCKET_NAME = "customer-behavior-lakehouse1"
RAW_PATH = f"s3://{BUCKET_NAME}/raw/"
BRONZE_PATH = f"s3://{BUCKET_NAME}/bronze/"

# Process CSV tables
csv_tables = ["customers", "orders", "products", "order_items", "reviews", "sessions"]
for table in csv_tables:
    df = spark.read.option("header", "true").option("inferSchema", "true").csv(f"{RAW_PATH}{table}.csv")
    df.write.mode("overwrite").parquet(f"{BRONZE_PATH}{table}/")

# Process Firehose streaming events (JSON)
events_df = spark.read.option("recursiveFileLookup", "true").json(
    f"s3://{BUCKET_NAME}/raw/streaming/events/2026/07/06/08/"
)
events_df.write.mode("overwrite").parquet(f"{BRONZE_PATH}events/")
```

Click **Save** then **Run**.

**Monitor the job:**
- Go to **Runs** tab
- Wait for status to change from `Running` → `Succeeded` (~3–5 minutes)

> 📌 **[INSERT SCREENSHOT: Glue Jobs list showing all jobs]**
> `![Glue Jobs](/result/AWS Glue/AWS Glue Jobs.jpg)`

**Validate Bronze output:**
```bash
aws s3 ls s3://customer-behavior-lakehouse1/bronze/ --recursive | head -20
```

Expected: Parquet files in each table subdirectory.

> 📌 **[INSERT SCREENSHOT: S3 Bronze layer with Parquet files]**
> `![S3 Bronze](/result/S3/S3 Bronze.jpg)`

---

## 3.4 Create Glue ETL Job 2: Bronze → Silver

**AWS Console → AWS Glue → ETL Jobs → Create job → Script editor**

| Field | Value |
|-------|-------|
| Name | `bronze-to-silver-job` |
| IAM Role | `AWSGlueServiceRole-lakehouse` |
| Glue version | Glue 4.0 |
| Worker type | G.1X |
| Number of workers | 2 |
| Script path | `s3://customer-behavior-lakehouse1/scripts/bronze_to_silver_job.py` |

**Job script (`bronze_to_silver_job.py`) key logic:**

```python
BRONZE_PATH = f"s3://{BUCKET_NAME}/bronze/"
SILVER_PATH = f"s3://{BUCKET_NAME}/silver/"

tables = ["customers", "orders", "products", "order_items", "reviews", "sessions", "events"]

for table in tables:
    df = spark.read.parquet(f"{BRONZE_PATH}{table}/")
    
    # 1. Remove duplicates
    df = df.dropDuplicates()
    
    # 2. Normalize column names (lowercase, underscore)
    for old_col in df.columns:
        new_col = old_col.strip().lower().replace(" ", "_").replace("-", "_")
        if old_col != new_col:
            df = df.withColumnRenamed(old_col, new_col)
    
    # 3. Trim whitespace from string columns
    for field in df.schema.fields:
        if isinstance(field.dataType, StringType):
            df = df.withColumn(field.name, trim(col(field.name)))
    
    # 4. Parse date/time columns
    for column_name in df.columns:
        if any(kw in column_name.lower() for kw in ["date", "time", "timestamp"]):
            df = df.withColumn(column_name, to_timestamp(col(column_name)))
    
    df.write.mode("overwrite").parquet(f"{SILVER_PATH}{table}/")
```

Run the job and wait for **Succeeded** status (~5–8 minutes).

**Validate Silver output:**
```bash
aws s3 ls s3://customer-behavior-lakehouse1/silver/ --recursive | head -20
```

> 📌 **[INSERT SCREENSHOT: S3 Silver layer]**
> `![S3 Silver](/result/S3/S3 Silver.jpg)`

---

## 3.5 Create Glue ETL Job 3: Silver → Gold

This is the most critical job - it computes business KPIs and registers the results as external tables in the Glue Data Catalog, making them queryable by Athena.

| Field | Value |
|-------|-------|
| Name | `silver-to-gold-job` |
| IAM Role | `AWSGlueServiceRole-lakehouse` |
| Glue version | Glue 4.0 |
| Worker type | G.1X |
| Number of workers | 2 |
| Script path | `s3://customer-behavior-lakehouse1/scripts/silver_to_gold_job.py` |

**Job script (`silver_to_gold_job.py`) key logic:**

```python
DATABASE_NAME = "customer_behavior_catalog_db"
SILVER_PATH = f"s3://{BUCKET_NAME}/silver/"
GOLD_PATH = f"s3://{BUCKET_NAME}/gold/"

glue = boto3.client("glue")

# Read Silver tables
events = spark.read.parquet(f"{SILVER_PATH}events/")
orders = spark.read.parquet(f"{SILVER_PATH}orders/")
orders = orders.withColumn("order_date", to_date(col("order_time")))

# Compute KPI aggregations
daily_revenue = orders.groupBy("order_date").agg(sum("total_usd").alias("total_revenue"))
payment_summary = orders.groupBy("payment_method").agg(
    count("order_id").alias("total_orders"),
    sum("total_usd").alias("total_revenue"),
    avg("total_usd").alias("avg_order_value")
)
country_revenue = orders.groupBy("country").agg(...)
device_summary = orders.groupBy("device").agg(...)
source_summary = orders.groupBy("source").agg(...)
event_summary = events.groupBy("event_type").agg(count("*").alias("total_events"))
dashboard_summary = orders.agg(
    countDistinct("order_id").alias("total_orders"),
    countDistinct("customer_id").alias("total_customers"),
    sum("total_usd").alias("total_revenue"),
    avg("total_usd").alias("avg_order_value")
).withColumn("total_events", lit(events.count()))

# Write to Gold + register in Glue Catalog
write_gold_table("daily_revenue", daily_revenue)
write_gold_table("payment_summary", payment_summary)
write_gold_table("country_revenue", country_revenue)
write_gold_table("device_summary", device_summary)
write_gold_table("source_summary", source_summary)
write_gold_table("event_summary", event_summary)
write_gold_table("dashboard_summary", dashboard_summary)
```

The `write_gold_table()` function:
1. Writes Parquet to `s3://.../gold/<table_name>/`
2. Calls `glue.delete_table()` (if exists)
3. Calls `glue.create_table()` to register the schema in Glue Data Catalog

Run the job and wait for **Succeeded** (~8–12 minutes).

**Validate Gold output:**
```bash
# Check S3 Gold
aws s3 ls s3://customer-behavior-lakehouse1/gold/ --recursive | head -30

# Check Glue Catalog tables
aws glue get-tables --database-name customer_behavior_catalog_db \
    --query "TableList[].Name"
```

Expected: 7 table names returned: `daily_revenue`, `payment_summary`, `country_revenue`, `device_summary`, `source_summary`, `event_summary`, `dashboard_summary`.

> 📌 **[INSERT SCREENSHOT: Glue Catalog Tables registered]**
> `![Glue Tables](/result/AWS Glue/Glue Tables.jpg)`

> 📌 **[INSERT SCREENSHOT: S3 Gold layer]**
> `![S3 Gold](/result/S3/S3 Gold.jpg)`

---

## 3.6 Test & Error Handling

**Check job logs if a run fails:**

**AWS Console → AWS Glue → Jobs → [job name] → Runs → [failed run] → Error logs**

Or via CLI:
```bash
# Get job run details
aws glue get-job-runs --job-name silver-to-gold-job \
    --query "JobRuns[0].{Status:JobRunState,Error:ErrorMessage,Start:StartedOn}"
```

**Common errors:**

| Error | Cause | Fix |
|-------|-------|-----|
| `EntityNotFoundException: Database not found` | Glue catalog database not created yet | Complete Step 3.1 first |
| `AccessDeniedException` | IAM role missing S3 or Glue permissions | Attach required policies to `AWSGlueServiceRole-lakehouse` |
| `AnalysisException: Path does not exist` | Bronze/Silver data not yet written | Run Job 1 before Job 2, Job 2 before Job 3 |
| Job timeout | Large dataset / insufficient workers | Increase Number of workers to 4 |

✅ **Step 3 complete** - Proceed to [Step 4: Amazon Athena Queries](../5.4.4-Athena/)
