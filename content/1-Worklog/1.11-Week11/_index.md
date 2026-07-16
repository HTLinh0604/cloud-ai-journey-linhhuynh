---
title: "Week 11"
date: 2026-06-29
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

Weekly objectives:
- Build a Python script to generate mock customer interaction events.
- Deploy S3 buckets and configure secure access policies.
- Implement the first Glue ETL job to ingest raw data to Bronze.
- Create the second Glue ETL job for data cleaning and normalization.
- Develop the third Glue ETL job to aggregate KPIs into Gold tables and auto-register with the Glue Catalog.
- Configure Athena workgroups and validate business analytical queries.

Tasks to be deployed this week:

| Day | Task | Date |
|---|---|---|
| Monday | Implement the synthetic event generator script and configure secure S3 buckets. | Jun 29 |
| Tuesday | Create and run the raw-to-bronze Glue ETL job with schema enforcement. | Jun 30 |
| Wednesday | Implement the bronze-to-silver Glue job to deduplicate and normalize records. | Jul 1 |
| Thursday | Develop the silver-to-gold Glue job to create business tables and sync with the Data Catalog. | Jul 2 |
| Friday | Configure Athena Workgroups with query size thresholds and execute validation queries. | Jul 3 |

Weekly results achieved:
- Built the storage layer layout and generated 10,000 mock events.
- Created three Glue ETL jobs running PySpark transformations successfully.
- Registered Gold tier analytics tables directly into the Glue Data Catalog.
- Confirmed business query logic in Athena within budget thresholds.
- Saved deployment costs by avoiding Crawler jobs and using dynamic dynamic-frame metadata updates.
