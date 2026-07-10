---
title: "Step 4: Amazon Athena"
date: 2024-01-01
weight: 4
chapter: false
pre: " <b> 5.4.4 </b> "
---

# Step 4: Amazon Athena Queries

In this step, you will configure Amazon Athena to query the Gold-tier tables registered in the Glue Data Catalog, verify the pipeline results, and explore the data with sample business queries.

**Estimated time:** 15–20 minutes

---

## 4.1 Configure Athena Query Result Location

**AWS Console → Amazon Athena → Query editor → Settings → Manage**

| Field | Value |
|-------|-------|
| Query result location | `s3://customer-behavior-lakehouse1/athena-results/` |
| Encryption | SSE-KMS (or SSE-S3 for simplicity) |

Click **Save**.

> ⚠️ **Important:** Athena cannot run queries until a result location is configured. This step is mandatory.

---

## 4.2 Configure Athena Workgroup (FinOps)

Create a dedicated Workgroup with per-query cost controls:

**AWS Console → Athena → Administration → Workgroups → Create workgroup**

| Field | Value |
|-------|-------|
| Workgroup name | `lakehouse-wg` |
| Query result location | `s3://customer-behavior-lakehouse1/athena-results/` |
| Encrypt query results | ✅ SSE-S3 |
| Override client-side settings | ✅ Enabled |
| **Data usage controls** | |
| - Per-query limit | 1 GB |
| - Action if query exceeds limit | Cancel query |

Click **Create workgroup**.

> 💡 **FinOps note:** The 1 GB per-query scan limit acts as a safety net - any runaway query that would scan too much data is automatically cancelled before incurring excessive cost.

---

## 4.3 Select the Database

In the Athena Query Editor:
- **Data source**: `AwsDataCatalog`
- **Database**: `customer_behavior_catalog_db`
- **Workgroup**: `lakehouse-wg`

You should see 7 tables in the left panel: `daily_revenue`, `payment_summary`, `country_revenue`, `device_summary`, `source_summary`, `event_summary`, `dashboard_summary`.

---

## 4.4 Create External Tables (If Not Auto-Registered)

If the Glue ETL Job 3 did not auto-register tables (or for manual verification), run the CREATE TABLE statements from `athena_create_tables.sql`:

```sql
-- Dashboard Summary table
CREATE EXTERNAL TABLE IF NOT EXISTS dashboard_summary (
    total_orders    BIGINT,
    total_customers BIGINT,
    total_revenue   DOUBLE,
    avg_order_value DOUBLE,
    total_events    BIGINT
)
STORED AS PARQUET
LOCATION 's3://customer-behavior-lakehouse1/gold/dashboard_summary/';

-- Daily Revenue table
CREATE EXTERNAL TABLE IF NOT EXISTS daily_revenue (
    order_date    DATE,
    total_revenue DOUBLE
)
STORED AS PARQUET
LOCATION 's3://customer-behavior-lakehouse1/gold/daily_revenue/';

-- Event Summary table
CREATE EXTERNAL TABLE IF NOT EXISTS event_summary (
    event_type   STRING,
    total_events BIGINT
)
STORED AS PARQUET
LOCATION 's3://customer-behavior-lakehouse1/gold/event_summary/';

-- Country Revenue table
CREATE EXTERNAL TABLE IF NOT EXISTS country_revenue (
    country         STRING,
    total_orders    BIGINT,
    total_revenue   DOUBLE,
    avg_order_value DOUBLE
)
STORED AS PARQUET
LOCATION 's3://customer-behavior-lakehouse1/gold/country_revenue/';

-- Device Summary table
CREATE EXTERNAL TABLE IF NOT EXISTS device_summary (
    device          STRING,
    total_orders    BIGINT,
    total_revenue   DOUBLE,
    avg_order_value DOUBLE
)
STORED AS PARQUET
LOCATION 's3://customer-behavior-lakehouse1/gold/device_summary/';

-- Payment Summary table
CREATE EXTERNAL TABLE IF NOT EXISTS payment_summary (
    payment_method  STRING,
    total_orders    BIGINT,
    total_revenue   DOUBLE,
    avg_order_value DOUBLE
)
STORED AS PARQUET
LOCATION 's3://customer-behavior-lakehouse1/gold/payment_summary/';

-- Source Summary table
CREATE EXTERNAL TABLE IF NOT EXISTS source_summary (
    source          STRING,
    total_orders    BIGINT,
    total_revenue   DOUBLE,
    avg_order_value DOUBLE
)
STORED AS PARQUET
LOCATION 's3://customer-behavior-lakehouse1/gold/source_summary/';
```

---

## 4.5 Run Business Queries

Execute the following queries from `athena_queries.sql` to verify the pipeline results:

**Query 1: Overall dashboard metrics**
```sql
SELECT * FROM dashboard_summary;
```

> 📌 **[INSERT SCREENSHOT: Athena Dashboard Summary result]**
> `![Dashboard Summary](/result/Athenas/Dashboard Summary.jpg)`

**Query 2: Daily revenue trend (ordered by date)**
```sql
SELECT * FROM daily_revenue ORDER BY order_date;
```

> 📌 **[INSERT SCREENSHOT: Athena daily revenue query result]**
> `![Daily Revenue Athena](/result/Athenas/daily revenue.jpg)`

> 📌 **[INSERT SCREENSHOT: Daily Revenue CSV result]**
> `![Daily Revenue Result](/result/Athenas/result_daily_revenue.jpg)`

**Query 3: Top events by frequency**
```sql
SELECT * FROM event_summary ORDER BY total_events DESC;
```

> 📌 **[INSERT SCREENSHOT: Athena Event Summary result]**
> `![Event Summary](/result/Athenas/Event Summary.jpg)`

**Query 4: Revenue by country (top countries)**
```sql
SELECT * FROM country_revenue ORDER BY total_revenue DESC LIMIT 10;
```

**Query 5: Revenue by payment method**
```sql
SELECT * FROM payment_summary ORDER BY total_revenue DESC;
```

**Query 6: Revenue by device type**
```sql
SELECT * FROM device_summary ORDER BY total_revenue DESC;
```

**Query 7: Revenue by traffic source**
```sql
SELECT * FROM source_summary ORDER BY total_revenue DESC;
```

---

## 4.6 Check Metrics & Cost

After running queries, check:

**Data scanned per query:**

In Athena Query Editor, after each query completes, look at the **Data scanned** metric shown below the results. With Parquet format and no partitioning, expect:
- Small Gold tables (~100 KB – 5 MB) → data scanned ≈ same size
- Much less than if querying raw CSV/JSON directly

**CloudWatch metrics for Athena:**
```bash
aws cloudwatch get-metric-statistics \
    --namespace AWS/Athena \
    --metric-name DataScannedInBytes \
    --dimensions Name=WorkGroup,Value=lakehouse-wg \
    --start-time 2026-07-10T00:00:00Z \
    --end-time 2026-07-11T00:00:00Z \
    --period 86400 \
    --statistics Sum
```

---

## 4.7 Test Error Scenarios

**Test 1: Query a non-existent table**
```sql
SELECT * FROM non_existent_table;
```
Expected error: `Table not found` - Athena returns a clear error message.

**Test 2: Trigger cost limit (workgroup protection)**
```sql
-- Query the raw Silver layer directly (larger dataset)
SELECT * FROM silver_orders LIMIT 1000;
```
If the Silver table is large enough to exceed 1 GB, Athena will cancel the query with: `Query cancelled - data usage limit exceeded`.

---

## 4.8 Expected Results Summary

| Table | Expected Row Count | Key Insight |
|-------|-------------------|-------------|
| `dashboard_summary` | 1 row | Total orders, customers, revenue, avg order value |
| `daily_revenue` | ~365 rows | Revenue trend per day for ~1 year of data |
| `event_summary` | ~5–8 rows | Top event types (page_view, add_to_cart, purchase, etc.) |
| `country_revenue` | ~7–10 rows | Revenue by country |
| `device_summary` | 3 rows | mobile, desktop, tablet |
| `payment_summary` | 3 rows | credit_card, paypal, bank_transfer |
| `source_summary` | 4 rows | organic, social, email, paid_ads |

✅ **Step 4 complete** - Proceed to [Step 5: Deploy Streamlit Dashboard on EC2](../5.4.5-EC2-Dashboard/)
