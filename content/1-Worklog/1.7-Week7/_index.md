---
title: "Week 7"
date: 2026-06-01
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

**Weekly objectives:**
- Understand AWS ETL analytics pipeline patterns and Medallion architectures.
- Build a prototype data lake using Amazon S3, Glue, and Athena.
- Explore Infrastructure-as-Code development using CDK stacks and CloudFormation.
- Design serverless event-driven workflows using Step Functions and EventBridge.

**Tasks to be deployed this week:**

| Day | Task | Date |
|---|---|---|
| Monday | Analyzed the Medallion data architecture, studying data states across Raw, Bronze, Silver, and Gold tiers. Researched object partitioning strategies to optimize S3 storage and Athena queries. | Jun 1 |
| Tuesday | Built a data lake prototype on S3. Uploaded raw CSV datasets, ran Glue Crawlers to register metadata schemas, and executed test SQL queries using Amazon Athena. | Jun 2 |
| Wednesday | Developed CDK stacks defining S3 buckets and IAM roles. Practiced synthesizing CDK applications into CloudFormation nested templates to deploy resources. | Jun 3 |
| Thursday (Office visit) | Deployed serverless orchestration workflows using AWS Step Functions. Configured Step Functions state machines with retry rules and error handling, and routed events using EventBridge. | Jun 4 |
| Friday | Reviewed cloud networking configurations, database types, and storage formats to prepare for the final workshop project design. | Jun 5 |

**Weekly results achieved:**
- **Monday:**
  - Result Achieved: Drafted a data lake folder layout structure and partitioning scheme using date prefixes.
  - Lesson: Partitioning S3 data by date ensures that query tools scan only relevant objects, reducing execution costs.
- **Tuesday:**
  - Result Achieved: Verified active Glue Data Catalog tables and successful Athena query results against S3 objects.
  - Lesson: S3 + Glue + Athena forms a serverless query engine requiring zero cluster management, scaling query costs with use.
- **Wednesday:**
  - Result Achieved: Compiled CDK scripts that generated and deployed CloudFormation stacks successfully.
  - Lesson: Defining resources in CDK allows programmatic schema validations, helping to enforce standards across development teams.
- **Thursday (Office visit):**
  - Result Achieved: Active state machine running multi-step tasks, and custom EventBridge routing rules.
  - Lesson: Step Functions orchestrates serverless steps with built-in retry handling. EventBridge routes events across resources without coupling.
- **Friday:**
  - Result Achieved: Completed network layout blueprints and security group chained profiles for the final project VPC.
  - Lesson: A secure network layout with private subnets is the foundation of cloud architecture. Gateway endpoints keep data traffic within internal channels.

