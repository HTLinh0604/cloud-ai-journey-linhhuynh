---
title: "Week 8"
date: 2026-06-08
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

Weekly objectives:
- Explore local emulation of AWS environments using LocalStack and Floci.
- Research modern data engineering patterns and Medallion architectures.
- Create the system design for the final project data pipeline.
- Build a local data processing prototype using PySpark.
- Analyze the operational roles of all pipeline components.

Tasks to be deployed this week:

| Day | Task | Date |
|---|---|---|
| Monday | Set up LocalStack and Floci for local simulation of S3, Lambda, and DynamoDB. | Jun 8 |
| Tuesday | Research Medallion quality layers, schema evolution, and pipeline observability. | Jun 9 |
| Wednesday | Design the project data pipeline architecture and choose integration services. | Jun 10 |
| Thursday | Build a local end-to-end prototype using mock events and PySpark transformation code. | Jun 11 |
| Friday | Conduct a detailed component analysis for the ingestion, storage, and processing layers. | Jun 12 |

Weekly results achieved:
- Established a zero-cost local AWS development and test framework.
- Defined the project's medallion architecture using Firehose, Glue, and Athena.
- Verified data processing scripts locally using a PySpark prototype.
- Mapped all metadata schemas and storage locations across data quality tiers.
