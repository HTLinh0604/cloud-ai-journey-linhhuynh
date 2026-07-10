---
title: "Step 2: S3 & Data Upload"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 5.4.2 </b> "
---

# Step 2: S3 Buckets & Data Upload

In this step, you will create the S3 bucket with the Medallion Architecture prefix structure, configure bucket policies, and upload the sample data files.

**Estimated time:** 20–30 minutes

---

## 2.1 Create the S3 Bucket

**AWS Console → S3 → Create bucket**

| Field | Value |
|-------|-------|
| Bucket name | `customer-behavior-lakehouse1` |
| AWS Region | `us-east-1` |
| Object Ownership | ACLs disabled (recommended) |
| Block all public access | ✅ Enabled (keep all blocks on) |
| Bucket versioning | Enable (recommended for Bronze tier) |
| Default encryption | Server-side encryption with AWS KMS (SSE-KMS) |
| AWS KMS key | AWS managed key (`aws/s3`) or create a Customer Managed Key |

Click **Create bucket**.

> 📌 **[INSERT SCREENSHOT: S3 Raw data overview]**
> `![S3 Raw](/result/S3/S3 Raw - dữ liệu gốc.jpg)`

---

## 2.2 Create the Folder Structure

Inside the bucket, create the following top-level folders (S3 "prefixes"):

```bash
aws s3api put-object --bucket customer-behavior-lakehouse1 --key raw/
aws s3api put-object --bucket customer-behavior-lakehouse1 --key bronze/
aws s3api put-object --bucket customer-behavior-lakehouse1 --key silver/
aws s3api put-object --bucket customer-behavior-lakehouse1 --key gold/
aws s3api put-object --bucket customer-behavior-lakehouse1 --key athena-results/
```

Or via Console: In the bucket, click **Create folder** for each of: `raw`, `bronze`, `silver`, `gold`, `athena-results`.

---

## 2.3 Upload Sample Data Files to Raw

Upload all 6 CSV files to the `raw/` prefix:

```bash
# Upload all CSV files at once
aws s3 cp customers.csv s3://customer-behavior-lakehouse1/raw/customers.csv
aws s3 cp orders.csv s3://customer-behavior-lakehouse1/raw/orders.csv
aws s3 cp products.csv s3://customer-behavior-lakehouse1/raw/products.csv
aws s3 cp order_items.csv s3://customer-behavior-lakehouse1/raw/order_items.csv
aws s3 cp reviews.csv s3://customer-behavior-lakehouse1/raw/reviews.csv
aws s3 cp sessions.csv s3://customer-behavior-lakehouse1/raw/sessions.csv

# Verify uploads
aws s3 ls s3://customer-behavior-lakehouse1/raw/
```

> 📌 **[INSERT SCREENSHOT: Raw CSV files uploaded in S3]**
> `![S3 Raw data](/result/S3/S3 Raw - dữ liệu gốc.jpg)`

---

## 2.4 Create Athena Results Prefix

Athena requires a dedicated S3 location to store query results. The `athena-results/` prefix is already created in step 2.2. Note the full S3 path:

```
s3://customer-behavior-lakehouse1/athena-results/
```

This will be used when configuring Athena in Step 4.

---

## 2.5 IAM Role for Glue ETL Jobs

Create an IAM role that Glue ETL jobs will use to read from and write to S3.

**AWS Console → IAM → Roles → Create role**

| Field | Value |
|-------|-------|
| Trusted entity type | AWS service |
| Service | Glue |
| Use case | Glue |

**Add permissions - attach these policies:**
- `AWSGlueServiceRole` (managed)
- `AmazonS3FullAccess` (for workshop simplicity)
- `AmazonAthenaFullAccess` (for Glue → Catalog registration in silver_to_gold_job)

**Role name:** `AWSGlueServiceRole-lakehouse`

> ⚠️ **Least-privilege note:** In production, replace `AmazonS3FullAccess` with a custom policy that restricts `s3:GetObject` to the Bronze prefix and `s3:PutObject` to the Silver prefix for Job 1, and vice versa for Job 2. This prevents cross-tier write access.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:ListBucket"],
      "Resource": [
        "arn:aws:s3:::customer-behavior-lakehouse1/bronze/*",
        "arn:aws:s3:::customer-behavior-lakehouse1"
      ]
    },
    {
      "Effect": "Allow",
      "Action": ["s3:PutObject", "s3:DeleteObject"],
      "Resource": "arn:aws:s3:::customer-behavior-lakehouse1/silver/*"
    }
  ]
}
```

---

## 2.6 Test Streaming Ingestion (Optional - Firehose)

If you want to test the Firehose streaming path:

**AWS Console → Amazon Data Firehose → Create Firehose stream**

| Field | Value |
|-------|-------|
| Source | Direct PUT |
| Destination | Amazon S3 |
| Firehose stream name | `lakehouse-event-stream` |
| S3 bucket | `customer-behavior-lakehouse1` |
| S3 prefix | `raw/streaming/events/` |
| S3 error prefix | `raw/streaming/errors/` |
| Buffer size | 1 MB |
| Buffer interval | 60 seconds |

**Test with AWS CLI:**
```bash
aws firehose put-record \
    --delivery-stream-name lakehouse-event-stream \
    --record '{"Data": "{\"event_type\": \"page_view\", \"customer_id\": \"CUST-0001\", \"product_id\": \"PROD-042\", \"timestamp\": \"2026-07-10T10:00:00Z\"}\n"}'
```

Wait 60–90 seconds, then verify data appeared in S3:
```bash
aws s3 ls s3://customer-behavior-lakehouse1/raw/streaming/ --recursive
```

> 📌 **[INSERT SCREENSHOT: Firehose data delivered to S3]**
> `![Firehose in S3](/result/S3/FirehoseStreaming đã đổ data vào S3.jpg)`

---

## 2.7 Validation

```bash
# List all prefixes to confirm structure
aws s3 ls s3://customer-behavior-lakehouse1/ --recursive --human-readable --summarize | head -30

# Check bucket versioning
aws s3api get-bucket-versioning --bucket customer-behavior-lakehouse1

# Check encryption
aws s3api get-bucket-encryption --bucket customer-behavior-lakehouse1
```

Expected: versioning `Enabled`, encryption `aws:kms`.

✅ **Step 2 complete** - Proceed to [Step 3: AWS Glue ETL Jobs](../5.4.3-Glue/)
