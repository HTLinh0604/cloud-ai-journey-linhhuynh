---
title: "Week 3"
date: 2026-05-04
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

**Weekly objectives:**
- Install, configure, and use the AWS CLI to manage resources with advanced query filters.
- Understand Amazon DynamoDB and NoSQL database modeling concepts.
- Deploy global caching using CloudFront and configure Lambda@Edge.
- Build custom network infrastructure with public subnets and deploy an EC2 web server.
- Develop serverless apps with AWS Lambda and deploy infrastructure using AWS CDK.

**Tasks to be deployed this week:**

| Day | Task | Date |
|---|---|---|
| Monday (Office visit) | Installed the AWS CLI and configured credential profiles. Practiced complex resource queries using JMESPath filters. Created a custom VPC, subnet, route table, Internet Gateway, and launched an EC2 instance running Apache web server using user data. | May 4 |
| Tuesday (Office visit) | Deployed a DynamoDB table and studied partition and sort key design. Configured Amazon CloudFront distribution to cache static assets and researched Lambda@Edge request manipulation. | May 5 |
| Wednesday (Office visit) | Created serverless Python Lambda functions, configuring memory limits and execution timeouts. Initialized an AWS CDK application in TypeScript, defining standard S3 constructs. | May 6 |
| Thursday | Practiced AWS CLI commands to synchronize local directories with S3 buckets. Used configuration flags to filter files and set storage classes during upload. | May 7 |
| Friday | Configured S3 lifecycle policies and verified transition rules. Explored AWS Toolkit for VS Code to browse Lambda functions and execute test queries locally. | May 8 |

**Weekly results achieved:**
- **Monday (Office visit):**
  - Result Achieved: Configured AWS CLI profiles, queried active instances, and verified the Apache web page was accessible publicly.
  - Lesson: Automation via CLI is faster than console configuration. VPC design forms the basic network isolation layer for cloud resources.
- **Tuesday (Office visit):**
  - Result Achieved: Active DynamoDB table with composite primary key, and CloudFront distribution caching objects.
  - Lesson: DynamoDB scales horizontally through key distribution. CloudFront caching reduces load on origins and decreases latency.
- **Wednesday (Office visit):**
  - Result Achieved: Active Lambda function and synthesized CDK template generating CloudFormation outputs.
  - Lesson: Lambda provides serverless scalability. CDK allows defining infrastructure using standard programming languages.
- **Thursday:**
  - Result Achieved: Wrote a script to sync local files to S3, verify checksums, and list bucket contents via CLI.
  - Lesson: Scripting S3 data management via CLI is essential for automated backup pipelines and data ingestion processes.
- **Friday:**
  - Result Achieved: Applied lifecycle transition policies and successfully ran local Lambda function tests using the IDE toolkit.
  - Lesson: IDE tools improve developer productivity by allowing local debugging of serverless functions before deployment.

