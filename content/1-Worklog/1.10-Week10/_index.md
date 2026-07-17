---
title: "Week 10"
date: 2026-06-22
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

**Weekly objectives:**
- Research Data Engineering best practices including DataOps and schema drift handling.
- Participate in the AWS office event to study real-world cost optimization strategies.
- Plan the codebase modules and workflow tasks for the pipeline project.
- Configure the local development environment and initialize the Git repository.

**Tasks to be deployed this week:**

| Day | Task | Date |
|---|---|---|
| Monday | Read technical documentation regarding DataOps principles and metadata management. Analyzed schema drift patterns and options for capturing unexpected fields in data pipelines. | Jun 22 |
| Tuesday | Reviewed the project data architecture layout. Validated S3 object prefix partitioning formats and verified schema structures for data catalog consistency. | Jun 23 |
| Wednesday | Participated in the AWS technology sharing event at the Amazon office. Listened to sessions detailing cost optimization techniques and discussed pipeline patterns with solution architects. | Jun 24 |
| Thursday | Defined the software design specifications for the pipeline codebase. Divided the implementation into distinct modules, mapping out Python tasks and PySpark transformations. | Jun 25 |
| Friday | Set up the local virtual environment on the development machine. Installed PySpark library dependencies, configured local AWS CLI credentials, and initialized the Git repository. | Jun 26 |

**Weekly results achieved:**
- **Monday:**
  - Result Achieved: Formulated strategy specifications to isolate schema modifications into JSON columns.
  - Lesson: Planning for schema drift ensures that unexpected upstream source schema changes do not crash automated ETL pipelines.
- **Tuesday:**
  - Result Achieved: Completed the final architecture design blueprint with partition properties locked.
  - Lesson: Locking partition paths early prevents database schema conflicts and ensures consistent query behaviors.
- **Wednesday:**
  - Result Achieved: Gathered case study notes regarding partition projection configurations for Amazon Athena.
  - Lesson: Interactive networking with experienced architects reveals production failure modes and optimizations that are not documented.
- **Thursday:**
  - Result Achieved: Completed the software design plan listing the functional boundaries of each processing script.
  - Lesson: Breaking code into modular, single-responsibility files makes testing simpler and improves overall code maintainability.
- **Friday:**
  - Result Achieved: Configured active virtual environment and verified local PySpark script execution.
  - Lesson: A clean local development setup with virtual environment isolation prevents library dependency conflicts and enables rapid local testing.

