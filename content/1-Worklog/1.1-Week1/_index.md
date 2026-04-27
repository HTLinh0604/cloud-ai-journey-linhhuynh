---
title: "Week 1 Worklog"
date: 2026-04-27
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---

> **Week 1 — Igniting the Cloud AI Journey:** Onboarding to the AWS ecosystem, completing 5 credit-earning tasks, and building a solid cost monitoring foundation.

---

### Week 1 Objectives

* Create and configure an AWS account, earning **$200 in credits** through hands-on tasks.
* Get acquainted with AWS global infrastructure and core services: EC2, S3, IAM, VPC, RDS, Lambda, and Bedrock.
* Establish a comprehensive cost monitoring and control system (AWS Budgets, CloudWatch, Cost Explorer).
* Master foundational concepts: Cloud Computing models, AWS security, identity management (IAM), and networking (VPC).

---

### Week 1 Schedule

| Day | Tasks | Date | Reference |
| --- | ----- | ---- | --------- |
| **2** | - Create AWS account & receive $100 starter credit from AWS <br> - Complete **5 Tasks** to earn an additional $100 credit: <br>&emsp; + Task 1: Launch EC2 Instance (+$20) <br>&emsp; + Task 2: Amazon Bedrock Playground (+$20) <br>&emsp; + Task 3: Set up AWS Budgets (+$20) <br>&emsp; + Task 4: Create Lambda Web App (+$20) <br>&emsp; + Task 5: Create RDS Database (+$20) <br> - Topics studied: <br>&emsp; + Creating Your First AWS Account <br>&emsp; + Managing Costs with AWS Budgets <br>&emsp; + Getting Help with AWS Support <br>&emsp; + Access Management with AWS IAM <br>&emsp; + Networking Essentials with Amazon VPC | 20/04/2026 | [cloudjourney.awsstudygroup.com](https://cloudjourney.awsstudygroup.com/) |
| **4** | - Set up comprehensive **Basic Monitoring** system <br>&emsp; + Configure AWS Budgets (3 alert thresholds) <br>&emsp; + Create CloudWatch Alarms (Email / SMS / Slack) <br>&emsp; + Enable Cost Explorer & daily reports <br> - Study **Advanced Analytics** <br>&emsp; + Custom CloudWatch Metrics <br>&emsp; + Resource Tagging Strategy <br> - Build **Emergency Cost Control Protocol** <br> - Study AWS foundational theory <br> - Topics studied: <br>&emsp; + Compute Essentials with Amazon EC2 <br>&emsp; + Instance Profiling with IAM Roles for EC2 <br>&emsp; + Cloud Development with AWS Cloud9 <br>&emsp; + Static Website Hosting with Amazon S3 <br>&emsp; + Database Essentials with Amazon RDS | 22/04/2026 | [cloudjourney.awsstudygroup.com](https://cloudjourney.awsstudygroup.com/) |

---

### Task Details

#### Day 1 — Monday (2), 20/04/2026: Account Activation & Completing 5 Tasks

##### Creating an AWS Account — Earning $100 Credit

The very first step of this journey was registering for an AWS account. Upon successful creation and identity verification, the account automatically received **$100 in starter credits** from AWS.

---

##### Task 1: Launch EC2 Instance +$20 Credit

**Objective:** Create and manage a Virtual Machine on AWS Cloud.

**EC2 (Elastic Compute Cloud)** is AWS's flagship compute service, enabling the launch of virtual servers with flexible hardware configurations and operating systems.

Steps:
1. Go to **AWS Console** → "Explore AWS" widget → Select **Launch an instance using EC2**.
2. Click **Start activity**.
3. Set Instance name: `Test Instance` → Choose an appropriate AMI.
4. Keep default hardware configuration.
5. Create a new Key Pair: Name `first-kp` | Type **RSA** | Format **.pem**
6. Create a Security Group with default rules.
7. Review settings → **Launch Instance**.
8. **Clean up:** Terminate the instance after completion to avoid ongoing charges.

> **Key Takeaway:** Always clean up resources immediately after practice to optimize costs.

---

##### Task 2: Amazon Bedrock Playground +$20 Credit

**Objective:** Experience AI/ML with Foundation Models on AWS.

**Amazon Bedrock** is a fully managed service providing access to leading foundation models (Claude, Llama, Titan, etc.) through a unified API — no infrastructure management required.

Steps:
1. Access **Bedrock Console** → Select task **Use a foundation model in Amazon Bedrock**.
2. Select model: **Claude 3 Haiku** (ideal balance between performance and cost).
3. Fill in use case details and submit, then await approval. If encountering an authorization error, raise an **AWS Support Case** (Category: Bedrock Allowlisting).
4. Once approved: Write a test prompt → **Run** → Review response → **Finish**.

> **Key Takeaway:** Some AWS AI services require use case approval before activation — a Responsible AI measure to prevent misuse.

---

##### Task 3: Set up AWS Budgets +$20 Credit

**Objective:** Establish a cost monitoring and alerting system.

**AWS Budgets** allows setting cost thresholds with automatic notifications — an essential tool for financial governance on the cloud.

Steps:
1. Access **Budgets Console** → Select task **Set up a cost budget using AWS Budgets**.
2. Click **Start activity** → Configure budget parameters.
3. Enter notification email address → **Create budget**.
4. Budget created successfully with automated email alerts.

---

##### Task 4: Create Lambda Web App +$20 Credit

**Objective:** Build a serverless web application on AWS.

**AWS Lambda** is a serverless compute service — run code without managing servers, paying only for actual execution time.

Steps:
1. Access **Lambda Console** → Select task **Create a web app using AWS Lambda**.
2. Click **Start activity** → Choose **Use a blueprint** → **Getting started with Lambda HTTP**.
3. Set function name: `http-function-url-tutorial`.
4. Check **Acknowledgment** → **Create function** successfully.
5. **Clean up:** Delete the function after completion.

> **Key Takeaway:** Serverless architecture completely eliminates the need for server provisioning — ideal for workloads with unpredictable traffic patterns.

---

##### Task 5: Create RDS Database +$20 Credit

**Objective:** Set up a managed relational database on AWS.

**Amazon RDS (Relational Database Service)** manages the entire database lifecycle — backups, patching, scaling — freeing developers to focus on application logic.

Steps:
1. Access **RDS Console** → Select task **Create an Amazon RDS Database**.
2. Choose **Easy create** → Select engine: **Aurora (PostgreSQL Compatible)**.
3. **Create database** → Wait for status to change to **Available**.
4. **Clean up (in order):** Delete instance `database-1-instance-1` first, then delete cluster `database-1`.

> **Note:** Always delete the instance before the cluster to avoid dependency errors.

---

#### Day 2 — Wednesday (4), 22/04/2026: Monitoring, Analytics & Foundational Theory

##### Basic Monitoring — Cost Control Setup

**1. AWS Budgets (3-tier alert system)**

| Budget | Threshold | Alert Trigger |
|--------|-----------|--------------| 
| Budget 1 | $50/month | Alert at 80% ($40) |
| Budget 2 | $25/month | Alert at 50% ($12.5) |
| Budget 3 | $10/day | Alert at 100% ($10) |

**2. Billing Alerts via CloudWatch Alarms**

| Threshold | Notification Channel |
|-----------|---------------------|
| $25 | Email warning |
| $50 | Email + SMS |
| $75 | Email + SMS + Slack |

**3. Cost Explorer**
- Enable **daily cost reports** for real-time spending visibility.
- Set up **service-level breakdown** — analyze costs per service.
- Monitor **top 5 cost drivers** to quickly identify the largest expense sources.

---

##### Advanced Analytics

**Custom CloudWatch Metrics:**
Create custom metrics to monitor business-specific indicators beyond AWS default metrics.

**Resource Tagging Strategy:**
Apply consistent tags across all AWS resources to accurately allocate costs by team, project, and environment (dev/staging/prod).

---

##### Emergency Cost Control Protocol

**Immediate Resource Audit:**
Inventory all running resources when abnormal costs are detected.

**Emergency Shutdown Protocol:**
A procedure to rapidly shut down non-essential resources to prevent runaway costs — especially critical in a learning environment.

---

##### Foundational Knowledge

**Cloud Computing Overview:**
- Benefits of cloud computing: elasticity, pay-as-you-go, global reach.
- Service models: **IaaS, PaaS, SaaS**.
- Deployment models: Public Cloud, Private Cloud, Hybrid Cloud.

**AWS Global Infrastructure:**
- **Regions:** Geographically isolated areas (~30+ regions worldwide).
- **Availability Zones (AZs):** Separate data centers within a Region, ensuring High Availability.
- **Edge Locations:** Content distribution points (CDN) for CloudFront, reducing latency globally.

**AWS Security:**
- **Root Account:** Highest-privilege account — use only for initial setup, always protect with MFA.
- **IAM Users/Groups/Policies:** Fine-grained permissions following the **Least Privilege** principle.
- **MFA (Multi-Factor Authentication):** Mandatory for Root and high-privilege IAM users.

**Cost Management:**
- **AWS Free Tier:** 12 months of free usage for eligible services.
- **AWS Budgets:** Proactive cost alerting.
- **Cost Explorer:** Analyze spending trends over time by service.

**Core Services:**
- **Amazon S3:** Object storage with 99.999999999% (11 nines) durability.
- **Amazon EC2:** Flexible compute with diverse instance types.

---

##### Topics Learned

| Day | Topic |
|-----|-------|
| 20/4 | Creating Your First AWS Account |
| 20/4 | Managing Costs with AWS Budgets |
| 20/4 | Getting Help with AWS Support |
| 20/4 | Access Management with AWS Identity and Access Management (IAM) |
| 20/4 | Networking Essentials with Amazon Virtual Private Cloud (VPC) |
| 22/4 | Compute Essentials with Amazon Elastic Compute Cloud (EC2) |
| 22/4 | Instance Profiling with IAM Roles for EC2 |
| 22/4 | Cloud Development with AWS Cloud9 |
| 22/4 | Static Website Hosting with Amazon S3 |
| 22/4 | Database Essentials with Amazon Relational Database Service (RDS) |

---

### Week 1 Achievements

* **AWS Account** successfully created and configured with full security (MFA, IAM).
* **$200 AWS Credits** accumulated: $100 starter from AWS + $100 from 5 hands-on tasks.
* **5 core AWS services** practiced hands-on: EC2, Bedrock, Budgets, Lambda, RDS.
* **3-layer cost monitoring system** established: Budgets → CloudWatch Alarms → Cost Explorer.
* **Solid theoretical foundation** built: Cloud Computing, AWS Global Infrastructure, IAM, Networking.
* Understood and applied the **"Clean up after practice"** principle — always clean up resources after hands-on labs.

---

*Primary Reference: [First Cloud Journey — AWS Study Group](https://cloudjourney.awsstudygroup.com/)*
