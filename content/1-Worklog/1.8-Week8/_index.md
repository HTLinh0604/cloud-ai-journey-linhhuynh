---
title: "Week 8"
date: 2026-06-08
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

**Weekly objectives:**
- Set up a local development and test environment using LocalStack and Floci to emulate AWS cloud services.
- Research modern data engineering patterns including quality tiers in Medallion architectures and pipeline monitoring.
- Design the final project data pipeline architecture and choose integration services.
- Develop a local data transformation script prototype using PySpark processing engines.
- Document the operational responsibilities of each component in the final project pipeline.

**Tasks to be deployed this week:**

| Day | Task | Date |
|---|---|---|
| Monday | Install and configure LocalStack on the development machine. Set up the Floci tool to emulate Amazon S3 storage and AWS Lambda execution environments locally. | Jun 8 |
| Tuesday | Study Medallion data design practices to understand transitions between Bronze, Silver, and Gold quality layers. Define schema verification mechanisms to check incoming file configurations. | Jun 9 |
| Wednesday | Design the project data pipeline architecture. Select integration services including Kinesis Data Firehose for real-time streaming ingestion and Glue for ETL jobs. | Jun 10 |
| Thursday | Write a local PySpark processing script to clean mock customer interaction data. Test data parsing logic on the local development machine using containerized spark environments. | Jun 11 |
| Friday | Create a technical specification document describing the roles of S3, Glue, and Athena in the system. Map metadata schemas for each data transition stage in the project. | Jun 12 |

**Weekly results achieved:**
- **Monday:**
  - Result Achieved: Verified local S3 bucket creation and file upload capabilities using local emulators.
  - Lesson: Emulators provide a zero-cost environment to validate infrastructure logic locally before deploying to AWS.
- **Tuesday:**
  - Result Achieved: Completed research notes on schema evolution and data validation strategies for raw to structured tiers.
  - Lesson: Designing schema validations prevents malformed records from corrupting downstream production data lakes.
- **Wednesday:**
  - Result Achieved: Completed the draft architecture diagram mapping components from ingestion to analytics.
  - Lesson: Visualizing the data path helps identify data bottlenecks and aligns team understanding of data flows.
- **Thursday:**
  - Result Achieved: Executed a local PySpark job successfully converting raw CSV data into compressed Parquet files.
  - Lesson: Local PySpark testing ensures data transformation logic is correct before running expensive Glue jobs in cloud environments.
- **Friday:**
  - Result Achieved: Formulated schema mappings and data quality requirements for the ingestion, processing, and storage layers.
  - Lesson: Technical documentation ensures that the pipeline conforms to design requirements and serves as a reference for builders.

