---
title: "Week 11"
date: 2026-06-29
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

**Weekly objectives:**
- Write synthetic data generation scripts and provision S3 buckets.
- Develop AWS Glue ETL jobs in PySpark to process data through Medallion tiers.
- Configure metadata schema registrations in the Glue Data Catalog database.
- Deploy Athena workgroups and validate the correctness of business queries.

**Tasks to be deployed this week:**

| Day | Task | Date |
|---|---|---|
| Monday | Wrote a Python script to generate mock customer transaction logs in CSV format. Created S3 buckets and uploaded the datasets into the raw ingestion prefix. | Jun 29 |
| Tuesday | Coded `raw_to_bronze_job.py` using PySpark. Deployed the job on AWS Glue to cast data columns to correct types and write Snappy compressed Parquet to S3. | Jun 30 |
| Wednesday | Developed `bronze_to_silver_job.py` to handle data cleaning. Wrote PySpark transformations to deduplicate records by ID and normalize country values. | Jul 1 |
| Thursday | Coded `silver_to_gold_job.py` to calculate business KPIs. Configured the Glue jobs to write directly to S3 Gold and auto-register table metadata in the catalog. | Jul 2 |
| Friday | Configured the Amazon Athena workgroup, defining query output locations. Wrote and executed 7 SQL queries to verify data aggregates and cost metrics. | Jul 3 |

**Weekly results achieved:**
- **Monday:**
  - Result Achieved: Generated a CSV dataset containing ten thousand rows and verified successful upload to S3.
  - Lesson: Generating structured mock datasets enables developer isolation and testing of data parsing logic without using production data.
- **Tuesday:**
  - Result Achieved: Active Glue Job successfully converting raw CSV data into Bronze tier Parquet files.
  - Lesson: Storing data in Parquet format reduces storage footprint and speeds up read times during query operations.
- **Wednesday:**
  - Result Achieved: Active Glue Job transforming Bronze data into clean, deduplicated Silver tier datasets.
  - Lesson: Deduplicating records at the Silver layer prevents double-counting and ensures data quality for analytical tools.
- **Thursday:**
  - Result Achieved: Active Glue Job writing pre-aggregated Gold tables and registering them in the Glue Catalog.
  - Lesson: Performing business aggregations at the Gold layer simplifies querying, reducing data scans for reporting dashboards.
- **Friday:**
  - Result Achieved: Verified Athena SQL queries returning correct KPIs while scanning less than fifty megabytes per run.
  - Lesson: Partition pruning and columnar storage keep query scans small, keeping operational query costs minimal.

