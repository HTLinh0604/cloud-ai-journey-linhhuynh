---
title: "Week 12"
date: 2026-07-06
weight: 12
chapter: false
pre: " <b> 1.12. </b> "
---

Weekly objectives:
- Build and deploy the Streamlit analytics dashboard to an EC2 instance.
- Test, debug, and optimize dashboard loading times.
- Set up CloudWatch metric alarms and pipeline health dashboards.
- Author bilingual workshop guides and clean up all deployed AWS resources.

Tasks to be deployed this week:

| Day | Task | Date |
|---|---|---|
| Monday | Implement the Streamlit analytics application and run it on an EC2 instance. | Jul 6 |
| Tuesday | Test dashboard chart elements, troubleshoot query timeout issues, and add query caching. | Jul 7 |
| Wednesday | Configure CloudWatch alerts for Glue job failures and design a unified health dashboard. | Jul 8 |
| Thursday | Draft the first half of the bilingual workshop guide covering VPC, S3, Glue, and Athena. | Jul 9 |
| Friday | Write the second half of the workshop guide covering EC2 deployment and resource cleanup. | Jul 10 |

Weekly results achieved:
- Launched a functioning Streamlit dashboard with Plotly charts on an EC2 host.
- Optimized query response time from 12 seconds to under 1 second using data caching.
- Established automated notifications for pipeline failures via CloudWatch and SNS.
- Published a bilingual guide outlining deployment and cleanup steps for workshop users.
- Cleaned up all database, analytics, and host resources to ensure zero ongoing charges.
