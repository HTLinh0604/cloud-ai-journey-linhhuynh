---
title: "Week 4"
date: 2026-05-11
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

**Weekly objectives:**
- Use AWS CloudFormation templates to build repeatable infrastructure as code stacks.
- Configure AWS Glue Crawlers and manage metadata schemas in the Data Catalog.
- Optimize Amazon Athena querying using columnar formats.
- Provision managed RDS databases in private subnets with network security rules.

**Tasks to be deployed this week:**

| Day | Task | Date |
|---|---|---|
| Monday | Wrote CloudFormation templates defining S3 buckets and IAM roles. Practiced managing stacks through the CLI, exploring mappings, parameter values, and output exports. | May 11 |
| Tuesday | Created an AWS Glue Crawler to scan raw CSV files on S3. Configured crawler schedules and mapped detected schemas directly to the Glue Data Catalog database. | May 12 |
| Wednesday | Configured Athena Workgroups, setting query limits to control cost. Practiced running SELECT queries against Glue Data Catalog tables using SQL syntax. | May 13 |
| Thursday | Launched an Amazon RDS PostgreSQL database within private subnets of a custom VPC. Created security groups to restrict access to application servers only. | May 14 |
| Friday | Configured S3 VPC Gateway Endpoints to allow private connectivity from resources in private subnets without public internet traffic. Enabled VPC Flow Logs for security auditing. | May 15 |

**Weekly results achieved:**
- **Monday:**
  - Result Achieved: Deployed reusable CloudFormation template stack and verified resource creation via CLI.
  - Lesson: CloudFormation templates provide a single source of truth for resource deployments, ensuring repeatable configurations.
- **Tuesday:**
  - Result Achieved: Active Glue Crawler and registered Data Catalog tables containing automatically detected schemas.
  - Lesson: Glue Crawlers automate schema discovery, keeping data catalog metadata synchronized with physical storage.
- **Wednesday:**
  - Result Achieved: Configured Athena Workgroup with query limit alerts, and verified SQL query results.
  - Lesson: Athena workgroups enable resource separation and cost tracking by limiting maximum bytes scanned per query.
- **Thursday:**
  - Result Achieved: Active private RDS instance with restricted network policies and verified database connection.
  - Lesson: Placing databases in private subnets prevents external exposure. Chaining security groups restricts access to authorized services.
- **Friday:**
  - Result Achieved: Active S3 VPC Endpoint and verified private file access from private EC2 instance.
  - Lesson: Gateway endpoints allow traffic to S3 to remain inside the AWS network, improving security and reducing NAT gateway costs.

