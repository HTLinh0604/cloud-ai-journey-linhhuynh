---
title: "Week 9"
date: 2026-06-15
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

**Weekly objectives:**
- Finalize the end-to-end architecture blueprint and detail all component integrations.
- Analyze and calculate the estimated monthly cost for all resources using the AWS Pricing Calculator.
- Define scalability, fault tolerance, and security specifications for the pipeline components.
- Document service trade-offs and prepare technical flowcharts for the workshop.

**Tasks to be deployed this week:**

| Day | Task | Date |
|---|---|---|
| Monday | Confirmed the layers of the Medallion architecture, mapping data states from CSV logs to aggregated Gold Parquet tables. Defined S3 bucket structures for each data quality tier. | Jun 15 |
| Tuesday | Researched streaming ingestion options, comparing Kinesis Data Firehose with Apache Kafka. Studied Change Data Capture patterns for syncing databases with data lakes. | Jun 16 |
| Wednesday | Used the AWS Pricing Calculator to estimate monthly running costs for S3 storage, Glue ETL runs, Athena queries, and EC2 instances. Formulated cost optimization tactics. | Jun 17 |
| Thursday | Formulated security requirements including IAM roles with least privilege policies. Defined S3 server-side encryption settings and built-in retry options for Glue jobs. | Jun 18 |
| Friday | Completed technical flowcharts representing data transitions. Documented service trade-offs, choosing Firehose, Glue, and Athena to minimize costs and deployment complexity. | Jun 19 |

**Weekly results achieved:**
- **Monday:**
  - Result Achieved: Confirmed S3 folder hierarchies and mapped data schema transitions from Raw to Gold.
  - Lesson: Designing strict directory and schema structures prevents metadata chaos and query errors in the data catalog.
- **Tuesday:**
  - Result Achieved: Formulated evaluation report on Kinesis vs Kafka for streaming ingestion.
  - Lesson: Kinesis Firehose is fully managed and integrates natively with S3, reducing operational overhead compared to Kafka.
- **Wednesday:**
  - Result Achieved: Completed a cost estimation report showing monthly cost allocations and savings from Parquet formats.
  - Lesson: Columnar formats like Parquet significantly reduce query scanning, lowering Athena query costs by up to 85%.
- **Thursday:**
  - Result Achieved: Completed security permission matrices and active-backup configuration parameters for the pipeline.
  - Lesson: Securing bucket access via IAM roles instead of hardcoded credentials prevents credentials leaks.
- **Friday:**
  - Result Achieved: Completed technical documentation and deployment checklists ready for workshop implementation.
  - Lesson: Documenting trade-offs provides reference context for future architecture modifications and expansions.

