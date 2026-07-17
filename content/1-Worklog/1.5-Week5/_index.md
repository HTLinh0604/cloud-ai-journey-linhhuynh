---
title: "Week 5"
date: 2026-05-18
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

**Weekly objectives:**
- Use AWS CLI scripting to automate resource management for EC2, S3, and IAM.
- Build automated folder synchronization processes to copy local files to Amazon S3.
- Create S3 Lifecycle policies to optimize storage costs based on object age.
- Implement automated volume backup schedules using Amazon Data Lifecycle Manager.

**Tasks to be deployed this week:**

| Day | Task | Date |
|---|---|---|
| Monday | Mastered AWS CLI operations for EC2 instances, S3 buckets, and IAM roles. Wrote scripts to automate instance launches, key pair configurations, and user permission list queries. | May 18 |
| Tuesday | Developed a script to sync local backup folders with S3 buckets. Used configuration flags to filter files and apply Infrequent Access storage class to the uploaded objects. | May 19 |
| Wednesday | Configured S3 lifecycle policies using rule configuration files. Defined rules to move objects to S3 Standard-IA after 30 days and Glacier Instant Retrieval after 90 days. | May 20 |
| Thursday | Configured EBS Data Lifecycle Manager (DLM) to automate volume snapshot creations. Deployed snapshot schedules with 14-day retention rules targeting production volumes. | May 21 |
| Friday | Formulated a disaster recovery plan mapping RTO and RPO requirements. Practiced restoring EBS volumes from automated snapshots and verifying file systems. | May 22 |

**Weekly results achieved:**
- **Monday:**
  - Result Achieved: Verified script-based creation of development EC2 instances and IAM user configurations via terminal.
  - Lesson: Utilizing CLI commands in scripts increases deployment speed and accuracy, reducing manual configuration errors.
- **Tuesday:**
  - Result Achieved: Verified file uploads, directory synchronization, and check sum calculations via CLI.
  - Lesson: Sync scripts keep S3 backups updated with minimum bandwidth use by calculating file changes and avoiding duplicate uploads.
- **Wednesday:**
  - Result Achieved: Active S3 Lifecycle configuration applied to test buckets with rules verified.
  - Lesson: Lifecycle policies automate cost optimization by moving data to cheaper storage tiers as access frequency decreases.
- **Thursday:**
  - Result Achieved: Deployed DLM policy successfully automating volume snapshots on schedule.
  - Lesson: Deploying DLM policies ensures consistent volume backups, helping to meet data loss limits.
- **Friday:**
  - Result Achieved: Completed a recovery plan document and verified successful volume restoration from test snapshots.
  - Lesson: Backup verification is essential to ensure recovery readiness. Regular testing confirms snapshot data can be restored.

