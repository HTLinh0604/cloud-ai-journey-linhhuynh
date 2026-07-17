---
title: "Week 12"
date: 2026-07-06
weight: 12
chapter: false
pre: " <b> 1.12. </b> "
---

**Weekly objectives:**
- Develop a Streamlit visualization dashboard and deploy it to an Amazon EC2 instance.
- Optimize database queries and implement page-load caching techniques.
- Configure AWS CloudWatch alarms and SNS notifications to monitor pipeline health.
- Document step-by-step workshop procedures and clean up all deployed cloud resources.

**Tasks to be deployed this week:**

| Day | Task | Date |
|---|---|---|
| Monday | Developed the Streamlit dashboard script `app_beautiful.py` using Plotly charts. Deployed the app onto an Amazon EC2 instance and modified security group rules to allow ingress access. | Jul 6 |
| Tuesday | Tested chart rendering speed and resolved database query timeouts. Configured memory caching using Streamlit cache functions to reduce query execution frequency. | Jul 7 |
| Wednesday | Created CloudWatch alarms to monitor Glue job execution failure counts. Configured Amazon SNS to send email notifications when a pipeline failure is detected. | Jul 8 |
| Thursday | Drafted the first part of the bilingual workshop guide, detailing custom VPC setups, S3 directory hierarchies, and Glue catalog configurations. | Jul 9 |
| Friday | Completed the remaining sections of the workshop guide, describing EC2 deployment, monitoring, and resource cleanup. Terminated all databases, EC2 instances, and storage structures. | Jul 10 |

**Weekly results achieved:**
- **Monday:**
  - Result Achieved: Verified active Streamlit dashboard displaying revenue charts on the EC2 instance.
  - Lesson: Hosting dashboards on EC2 with customized security groups provides a dedicated environment for user access control.
- **Tuesday:**
  - Result Achieved: Reduced dashboard page reload times from twelve seconds to under one second using caching.
  - Lesson: Caching query results locally prevents database query exhaustion and improves the dashboard user experience.
- **Wednesday:**
  - Result Achieved: Verified active automated notifications during test failures of pipeline runs.
  - Lesson: Automated monitoring ensures that pipeline failures are detected immediately, reducing system downtime.
- **Thursday:**
  - Result Achieved: Completed the draft guide detailing step-by-step setup guides in English and Vietnamese.
  - Lesson: Documenting configurations step-by-step helps workshop participants deploy resources correctly without errors.
- **Friday:**
  - Result Achieved: Completed the final workshop guide, pushed code to GitHub, and verified zero running resources.
  - Lesson: Documenting clean-up steps ensures that participants can delete resources properly, preventing unexpected cloud costs.

