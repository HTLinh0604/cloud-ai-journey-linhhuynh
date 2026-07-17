---
title: "Week 1"
date: 2026-04-20
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---

**Weekly objectives:**
- Activate the AWS account and ensure promotional starter credits are correctly applied.
- Complete five core hands-on tasks to explore compute, database, and serverless architectures.
- Understand the fundamentals of Cloud Computing, Global Infrastructure, and security practices.
- Design and implement a multi-layered cost monitoring and resource tagging strategy.

**Tasks to be deployed this week:**

| Day | Task | Date |
|---|---|---|
| Monday (Office visit) | Created a new AWS account, resolved billing setup requirements, and activated the 100 USD starter credits. Deployed and verified a test EC2 instance using a custom key pair, explored the Claude 3 Haiku playground in Amazon Bedrock, configured cost warning thresholds in AWS Budgets, created a basic serverless Lambda function, and provisioned a PostgreSQL instance in Amazon RDS. | Apr 20 |
| Tuesday | Studied the core definitions and benefits of Cloud Computing, distinguishing between IaaS, PaaS, and SaaS models. Analyzed the AWS Global Infrastructure, comparing Regions, Availability Zones, and Edge Locations for latency and high availability. | Apr 21 |
| Wednesday (Office visit) | Configured Multi-Factor Authentication (MFA) for the root account. Created IAM users, assigned them to developers and administrators groups, and attached policies using the principle of least privilege. Set up CloudWatch billing alarms at 25 USD, 50 USD, and 75 USD thresholds integrated with SNS email alerts. | Apr 22 |
| Thursday | Researched Amazon S3 storage classes (Standard, Infrequent Access, Glacier, Deep Archive) and their durability features. Analyzed EC2 instance families (T3, M5, C5) to understand CPU, memory, and networking allocations for various workloads. | Apr 23 |
| Friday | Practiced creating S3 buckets, uploading files, and managing object access. Launched an EC2 instance via the console, configured a security group with specific port rules, and tested remote access. | Apr 24 |

**Weekly results achieved:**
- **Monday (Office visit):**
  - Result Achieved: Active AWS account with 200 USD total promotional credits. Successfully ran and terminated all five test resources without incurring any unexpected costs.
  - Lesson: Gained hands-on familiarity with the AWS Console interface and established the critical rule of immediately cleaning up practice resources to avoid billing surprises.
- **Tuesday:**
  - Result Achieved: Drafted a reference document comparing IaaS, PaaS, and SaaS use cases and mapped regional latency benchmarks.
  - Lesson: Selecting the right AWS region is crucial for latency optimization, data residency compliance, and service availability.
- **Wednesday (Office visit):**
  - Result Achieved: Secured root account with MFA and created non-root administrator users. Billing alarms configured and verified via email test notifications.
  - Lesson: Securing root access and using granular IAM users is the first line of defense in cloud security. Automated alarms prevent budget overruns during testing.
- **Thursday:**
  - Result Achieved: Completed a comparative spreadsheet of S3 classes and EC2 instance types.
  - Lesson: Choosing the correct storage class and instance family directly impacts performance and storage costs, allowing efficient cost-to-performance optimization.
- **Friday:**
  - Result Achieved: Verified file uploads on S3 and successful SSH connection to the EC2 instance.
  - Lesson: Gained practical, confidence-building experience in manual resource provisioning and networking security group configuration.

