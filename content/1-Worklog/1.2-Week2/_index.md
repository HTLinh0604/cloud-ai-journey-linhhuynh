---
title: "Week 2"
date: 2026-04-27
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

**Weekly objectives:**
- Configure Amazon S3 buckets with advanced options including versioning, encryption, and lifecycle policies.
- Understand EBS volume types, performance metrics, and snapshots management.
- Configure EBS Data Lifecycle Manager (DLM) to automate volume backup schedules.
- Set up Amazon RDS database instances securely within custom subnets.

**Tasks to be deployed this week:**

| Day | Task | Date |
|---|---|---|
| Monday | Created S3 buckets, enabled versioning for backup tracking, and configured default encryption (SSE-S3). Set up S3 Static Website Hosting to serve a simple HTML index and test website redirection. | Apr 27 |
| Tuesday | Created S3 Lifecycle Policies to automate object transitions and storage cost reduction. Configured transitions to Standard-IA after 30 days and Glacier Deep Archive after 90 days. | Apr 28 |
| Wednesday | Analyzed EBS volume types (gp3, io2, st1) focusing on IOPS and throughput behaviors. Created a gp3 volume, attached it to an EC2 instance, and created a manual snapshot. | Apr 29 |
| Thursday | Configured EBS Data Lifecycle Manager (DLM) to automate snapshot creation. Defined a daily backup policy with a 7-day retention period, targeting volumes with specific project tags. | Apr 30 |
| Friday | Provisioned an Amazon RDS PostgreSQL instance (db.t3.micro) inside a custom VPC DB Subnet Group. Configured security groups to block public access, restricting database traffic to the EC2 application security group. | May 1 |

**Weekly results achieved:**
- **Monday:**
  - Result Achieved: Configured S3 bucket with versioning and verified static website hosting via public endpoint.
  - Lesson: S3 versioning protects against accidental deletes by retaining previous file states. Default encryption secures data at rest without performance impact.
- **Tuesday:**
  - Result Achieved: Active S3 Lifecycle configuration applied to test buckets with rules verified.
  - Lesson: Automating object lifecycles prevents manual maintenance and optimizes storage costs automatically as data ages.
- **Wednesday:**
  - Result Achieved: Formatted and mounted a new gp3 volume to EC2, and verified snapshot creation.
  - Lesson: gp3 provides independent IOPS and throughput configuration, allowing cost savings compared to older gp2 volumes.
- **Thursday:**
  - Result Achieved: Active DLM policy successfully automating volume snapshots on schedule.
  - Lesson: Automating snapshots using DLM guarantees consistent backup policies, ensuring disaster recovery capability.
- **Friday:**
  - Result Achieved: Active private RDS instance with restricted network access and verified client connection.
  - Lesson: Restricting database access to specific application security groups is standard security practice, preventing unauthorized connection attempts.

