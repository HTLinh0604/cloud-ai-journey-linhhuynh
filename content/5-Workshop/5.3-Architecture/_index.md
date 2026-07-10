---
title: "Architecture Description"
date: 2024-01-01
weight: 3
chapter: false
pre: " <b> 5.3 </b> "
---

# Architecture Description

## Overall Architecture

> 📌 **[INSERT OVERALL ARCHITECTURE DIAGRAM HERE]**
> `![Overall Architecture](/images/2-Proposal/overall_architecture.png)`

The platform implements a **Serverless Medallion Data Lakehouse** pattern - data flows through four S3 tiers (Raw → Bronze → Silver → Gold), processed by AWS Glue ETL jobs, queried by Amazon Athena, and visualized on a Streamlit Dashboard hosted on EC2 within a VPC.

---

## Layer-by-Layer Description

### Layer 1: VPC & Networking

The entire platform runs within an **Amazon VPC** to ensure network isolation and security.

```
VPC: 10.0.0.0/16
 └── Public Subnet: 10.0.1.0/24 (us-east-1a)
      └── EC2 Instance (Streamlit Dashboard)
           └── Elastic IP (static public IP)
 └── Internet Gateway → attached to VPC
 └── Route Table → 0.0.0.0/0 → Internet Gateway
 └── Security Group (EC2):
      Inbound: port 22 (SSH), port 8501 (Streamlit)
      Outbound: all traffic
```

> 📌 **[INSERT VPC DIAGRAM: Your VPCs screenshot]**
> `![VPC](/result/VPC/Your VPCs..jpg)`

**Why VPC?** Running EC2 inside a VPC ensures the dashboard cannot be accessed from arbitrary internet sources. The Security Group acts as a stateful firewall - only explicitly allowed ports (22 for management, 8501 for Streamlit) are open.

---

### Layer 2: S3 Data Lake - Medallion Architecture

Four S3 buckets (or four prefixes within one bucket) form the data lake tiers:

```
s3://customer-behavior-lakehouse1/
├── raw/                          ← Original source data (CSV + streaming JSON)
│   ├── customers.csv
│   ├── orders.csv
│   ├── products.csv
│   ├── order_items.csv
│   ├── reviews.csv
│   ├── sessions.csv
│   └── streaming/events/2026/07/06/08/   ← Firehose delivered JSON
│
├── bronze/                       ← Converted to Parquet, no transformation
│   ├── customers/
│   ├── orders/
│   ├── products/
│   ├── order_items/
│   ├── reviews/
│   ├── sessions/
│   └── events/
│
├── silver/                       ← Cleansed, deduplicated, schema-normalized
│   └── [same table structure as bronze]
│
├── gold/                         ← Business KPI aggregations (registered in Glue Catalog)
│   ├── event_summary/
│   ├── daily_revenue/
│   ├── payment_summary/
│   ├── country_revenue/
│   ├── device_summary/
│   ├── source_summary/
│   └── dashboard_summary/
│
└── athena-results/               ← Athena query result storage
```

> 📌 **[INSERT SCREENSHOT: S3 Raw data]**
> `![S3 Raw](/result/S3/S3 Raw - dữ liệu gốc.jpg)`

> 📌 **[INSERT SCREENSHOT: S3 Bronze layer]**
> `![S3 Bronze](/result/S3/S3 Bronze.jpg)`

> 📌 **[INSERT SCREENSHOT: S3 Silver layer]**
> `![S3 Silver](/result/S3/S3 Silver.jpg)`

> 📌 **[INSERT SCREENSHOT: S3 Gold layer]**
> `![S3 Gold](/result/S3/S3 Gold.jpg)`

---

### Layer 3: Ingestion Layer

**Streaming Path (Firehose → S3 Raw):**
- Amazon API Gateway receives HTTP POST events from clients
- Events are proxied to Amazon Data Firehose
- Firehose buffers events (60 seconds or 1 MB) and delivers to `s3://.../raw/streaming/`
- A Lambda function can be attached to Firehose for inline transformation

> 📌 **[INSERT SCREENSHOT: Firehose data in S3]**
> `![Firehose streaming to S3](/result/S3/FirehoseStreaming đã đổ data vào S3.jpg)`

**Batch Path (Lambda → S3 Raw):**
- Amazon EventBridge Scheduler fires on a cron schedule
- Triggers a Lambda function that reads the source database
- Lambda extracts records and writes CSV/Parquet to `s3://.../raw/`

---

### Layer 4: Processing Layer - AWS Glue ETL

Three sequential Glue ETL jobs process data through the Medallion tiers:

**Job 1: `raw_to_bronze_job.py` - Raw → Bronze**

Reads CSV files from S3 Raw, converts to Parquet, and writes to Bronze.

```python
# Key logic: Read CSV with schema inference, write as Parquet
df = spark.read.option("header", "true").option("inferSchema", "true").csv(input_path)
df.write.mode("overwrite").parquet(output_path)
```

Also reads streaming JSON events from the Firehose-delivered path.

**Job 2: `bronze_to_silver_job.py` - Bronze → Silver**

Applies data quality transformations:
- `dropDuplicates()` - removes exact duplicate rows
- Column name normalization (lowercase, underscores)
- String trimming for all StringType columns
- Timestamp parsing for date/time columns

**Job 3: `silver_to_gold_job.py` - Silver → Gold**

Computes business KPI aggregations and registers results in the Glue Data Catalog:
- `event_summary` - count of events by type
- `daily_revenue` - total revenue per day
- `payment_summary` - orders and revenue by payment method
- `country_revenue` - orders and revenue by country
- `device_summary` - orders and revenue by device type
- `source_summary` - orders and revenue by traffic source
- `dashboard_summary` - overall totals (orders, customers, revenue, events)

> 📌 **[INSERT SCREENSHOT: AWS Glue Jobs list]**
> `![Glue Jobs](/result/AWS Glue/AWS Glue Jobs.jpg)`

> 📌 **[INSERT SCREENSHOT: Glue Database]**
> `![Glue Database](/result/AWS Glue/Glue Database.jpg)`

> 📌 **[INSERT SCREENSHOT: Glue Tables]**
> `![Glue Tables](/result/AWS Glue/Glue Tables.jpg)`

---

### Layer 5: Query Layer - Amazon Athena

Amazon Athena reads Gold-tier tables registered in the Glue Data Catalog and executes SQL queries serverlessly.

```sql
-- Example: Daily Revenue trend
SELECT * FROM daily_revenue ORDER BY order_date;

-- Example: Top countries by revenue
SELECT * FROM country_revenue ORDER BY total_revenue DESC;
```

> 📌 **[INSERT SCREENSHOT: Athena query result - Daily Revenue]**
> `![Athena Daily Revenue](/result/Athenas/daily revenue.jpg)`

> 📌 **[INSERT SCREENSHOT: Athena Dashboard Summary]**
> `![Athena Dashboard Summary](/result/Athenas/Dashboard Summary.jpg)`

---

### Layer 6: Visualization Layer - Streamlit Dashboard on EC2

The Streamlit application (`app_beautiful.py`) runs on an EC2 instance and queries Athena via `awswrangler`:

```python
import awswrangler as wr
import boto3

DATABASE = "customer_behavior_catalog_db"
ATHENA_OUTPUT = "s3://customer-behavior-lakehouse1/athena-results/"

@st.cache_data(ttl=600)
def load_table(table_name: str):
    return wr.athena.read_sql_query(
        sql=f"SELECT * FROM {table_name}",
        database=DATABASE,
        s3_output=ATHENA_OUTPUT,
        boto3_session=boto3.Session(region_name="us-east-1")
    )
```

> 📌 **[INSERT SCREENSHOT: EC2 Instance running]**
> `![EC2 Instance](/result/EC2/EC2 Instance.jpg)`

> 📌 **[INSERT SCREENSHOT: Streamlit Dashboard - Revenue Trend]**
> `![Revenue Trend](/result/DashBoard/Revenue Trend.png)`

> 📌 **[INSERT SCREENSHOT: Streamlit Dashboard - Top Performers]**
> `![Top Performers](/result/DashBoard/Top Performers.jpg)`

---

## Service Selection Rationale

| Service | Why Selected | Alternative Considered |
|---------|-------------|----------------------|
| **Amazon S3** | Cheapest durable object storage; pay per GB stored; no minimum; perfect for data lake | EFS (too expensive), EBS (not shared) |
| **AWS Glue** | Fully managed PySpark; pay per DPU-second; no cluster to provision | EMR (requires cluster management, higher cost) |
| **Amazon Athena** | Pay per TB scanned; Parquet + partitioning reduces scans 85%; no warehouse provisioning | Redshift ($700+/month for smallest cluster) |
| **Amazon Data Firehose** | Zero capacity planning; built-in buffering; natively writes to S3 | Kinesis Data Streams (requires shard management) |
| **AWS Lambda** | Pay per 100ms invocation; zero idle cost; perfect for event-driven transforms | EC2 worker (always-on cost, over-provisioned) |
| **Amazon EC2 (t3.micro)** | Free Tier eligible; sufficient for Streamlit web app | Fargate/App Runner (slightly more complex for this use case) |
| **EventBridge Scheduler** | Serverless cron; 14M free invocations/month; zero always-on cost | EC2 cron (requires always-on instance) |
| **Glue Data Catalog** | Free up to 1M objects; unified metadata for Athena; no separate metastore | AWS Glue Crawlers with schedule (costs DPU-hours per crawl) |
