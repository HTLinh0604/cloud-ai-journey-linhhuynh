---
title: "Week 2 Worklog"
date: 2026-05-06
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

> **Week 2 — Deepening Into AWS Services:** Expanding hands-on skills across CLI, serverless, storage, databases, infrastructure-as-code, and data analytics.

---

### Week 2 Objectives

* Master the **AWS CLI** for programmatic cloud resource management.
* Understand and apply **serverless computing** with AWS Lambda and event-driven architectures.
* Work with **NoSQL databases** (DynamoDB), **CDN** (CloudFront), and edge computing (Lambda@Edge).
* Practice **infrastructure automation** using AWS CDK and AWS CloudFormation.
* Explore **data engineering** workflows with AWS Glue and Amazon Athena.
* Gain hands-on experience: deploying web servers, S3 lifecycle management, and relational database provisioning.

---

### Week 2 Schedule

| Day | Topics Studied | Hands-on Practice | Date |
| --- | -------------- | ----------------- | ---- |
| **Mon** | AWS CLI · NoSQL with Amazon DynamoDB · CloudFront & Lambda@Edge | Deploy a simple web server · Create EC2, VPC, Subnet | 04/05/2026 |
| **Tue** | AWS Lambda · AWS CDK · AWS Toolkit for VS Code · Amazon EBS Data Lifecycle Manager | Upload files from local to S3 · Create S3 Bucket · Configure Lifecycle Policies | 05/05/2026 |
| **Wed** | AWS CloudFormation · AWS Glue & Amazon Athena | Initialize and configure a relational database (PostgreSQL/MySQL) | 06/05/2026 |

---

### Task Details

#### Day 1 — Monday, 04/05/2026: CLI, NoSQL, CDN & Edge Computing

##### Theory: AWS CLI

**AWS CLI (Command Line Interface)** is a unified tool that provides a consistent interface for interacting with all AWS services directly from the terminal — enabling automation and scripting of cloud workflows.

Key concepts covered:
- Installing and configuring AWS CLI (`aws configure` with Access Key, Secret, Region, Output format).
- Running common commands: `aws ec2 describe-instances`, `aws s3 ls`, `aws iam list-users`.
- Using `--query` and `--output` flags for filtering and formatting results.
- Creating **named profiles** for multi-account management.

> **Key Takeaway:** The AWS CLI is indispensable for DevOps automation — every resource that can be created in the Console can be managed via CLI.

---

##### Theory: NoSQL Databases with Amazon DynamoDB

**Amazon DynamoDB** is a fully managed, serverless NoSQL database delivering single-digit millisecond performance at any scale — ideal for high-traffic applications.

Key concepts covered:
- **Data model:** Tables, Items (rows), Attributes (columns); no fixed schema required.
- **Primary Keys:** Partition Key (simple) and Partition Key + Sort Key (composite).
- **Read/Write Capacity Modes:** Provisioned vs. On-Demand.
- **DynamoDB Streams:** Capture item-level changes for event-driven architectures.
- **Global Tables:** Multi-region, fully replicated tables for ultra-low latency worldwide.
- **DAX (DynamoDB Accelerator):** In-memory caching for microsecond read performance.

> **Key Takeaway:** DynamoDB excels in use cases requiring horizontal scalability, flexible schemas, and predictable single-millisecond latency (e.g., gaming leaderboards, session stores, IoT).

---

##### Theory: CloudFront & Lambda@Edge

**Amazon CloudFront** is a globally distributed **Content Delivery Network (CDN)** that caches and delivers content from **Edge Locations** closest to end users, minimizing latency.

**Lambda@Edge** extends AWS Lambda to run code at CloudFront edge locations — enabling request/response customization without routing traffic back to the origin.

Key concepts covered:
- CloudFront **distributions**, **origins** (S3, ALB, EC2, custom HTTP), and **behaviors**.
- **Cache policies** and **origin request policies** for fine-grained control.
- **HTTPS enforcement** and **custom SSL certificates** via AWS Certificate Manager (ACM).
- Lambda@Edge **triggers:** Viewer Request, Origin Request, Origin Response, Viewer Response.
- Common use cases: URL rewrites, A/B testing, authentication at the edge, image optimization.

---

##### Hands-on: Deploy Simple Web Server & Configure EC2, VPC, Subnet

**1. Create a VPC and Subnet:**

| Resource | Configuration |
|----------|--------------|
| VPC | CIDR: `10.0.0.0/16` |
| Public Subnet | CIDR: `10.0.1.0/24`, AZ: `ap-southeast-1a` |
| Internet Gateway | Attached to VPC |
| Route Table | Route `0.0.0.0/0` → Internet Gateway |

**2. Launch an EC2 Instance as a Web Server:**
1. Navigate to **EC2 Console** → **Launch Instance**.
2. Select **Amazon Linux 2023 AMI** (free tier eligible).
3. Choose instance type: `t2.micro`.
4. Place instance in the newly created VPC and public subnet.
5. Configure **Security Group:** Allow inbound `HTTP (port 80)` and `SSH (port 22)`.
6. Add **User Data script** to automatically install and start Apache:
   ```bash
   #!/bin/bash
   yum update -y
   yum install -y httpd
   systemctl start httpd
   systemctl enable httpd
   echo "<h1>Hello from AWS EC2 - Week 2!</h1>" > /var/www/html/index.html
   ```
7. Launch the instance and access the public IP to verify the web server is running.

**Clean up after practice:**
- **Terminate** the EC2 instance (EC2 Console → Instances → Terminate).
- **Delete** the Internet Gateway (detach from VPC first, then delete).
- **Delete** the Route Table, Subnet, and finally the VPC.

> ⚠️ Always clean up all resources after practice to avoid unexpected charges.

> **Key Takeaway:** Understanding VPC networking (subnets, route tables, Internet Gateways) is fundamental to deploying any internet-accessible resource on AWS.

---

#### Day 2 — Tuesday, 05/05/2026: Serverless, IaC & Storage Management

##### Theory: AWS Lambda

**AWS Lambda** is a serverless, event-driven compute service — run code in response to events without provisioning or managing servers.

Key concepts covered:
- **Execution model:** Function → Handler → Runtime (Node.js, Python, Java, Go, etc.).
- **Triggers:** API Gateway, S3 events, DynamoDB Streams, SQS, CloudWatch Events, SNS.
- **Concurrency:** Reserved concurrency vs. provisioned concurrency.
- **Layers:** Package shared libraries/dependencies to keep function code clean.
- **Environment Variables** and **Secrets Manager** integration for secure configuration.
- **Lambda URLs:** Direct HTTPS endpoints without needing API Gateway.
- Pricing: Pay per request + duration (128 MB–10 GB RAM, up to 15 min timeout).

> **Key Takeaway:** Lambda's event-driven model is the backbone of modern serverless architectures on AWS — deeply integrated with virtually every AWS service.

---

##### Theory: AWS CDK (Cloud Development Kit)

**AWS CDK** lets developers define cloud infrastructure using familiar programming languages (TypeScript, Python, Java, C#) — compiling to CloudFormation templates under the hood.

Key concepts covered:
- **Constructs:** Reusable cloud components (L1: raw CFN, L2: curated, L3: patterns).
- **Stacks:** Units of deployment, mapped 1:1 to CloudFormation stacks.
- **Apps:** Root-level CDK programs containing one or more stacks.
- Core workflow: `cdk init` → Define constructs → `cdk synth` → `cdk deploy`.
- Benefits over raw CloudFormation: Type safety, IDE autocompletion, logic/loops/conditionals.

---

##### Theory: AWS Toolkit for VS Code

The **AWS Toolkit for VS Code** is an IDE extension enabling developers to interact with AWS services directly from VS Code.

Features explored:
- Browse and invoke **Lambda functions** without leaving the editor.
- Manage **S3 buckets and objects** via the Explorer panel.
- Integrated **CloudFormation** and **CDK** template support with syntax validation.
- Local debugging of Lambda functions using **SAM CLI** integration.
- Credentials management via **AWS Profiles**.

---

##### Theory: Amazon EBS Data Lifecycle Manager

**Amazon EBS Data Lifecycle Manager (DLM)** automates the creation, retention, and deletion of **EBS Snapshots** — the backup mechanism for EC2 volumes.

Key concepts covered:
- **Lifecycle policies:** Schedule snapshot creation (hourly, daily, weekly).
- **Retention rules:** Keep last N snapshots or retain for N days.
- **Cross-region copy:** Automatically replicate snapshots to a disaster recovery region.
- **Fast Snapshot Restore (FSR):** Pre-warm snapshots for immediate, full-performance volume restoration.

> **Key Takeaway:** DLM is the "set it and forget it" backup strategy for EBS — always configure DLM policies in production to ensure data durability.

---

##### Hands-on: S3 — Upload Files, Create Bucket & Configure Lifecycle Policies

**1. Create an S3 Bucket:**
```bash
aws s3api create-bucket \
  --bucket my-week2-bucket-$(date +%s) \
  --region ap-southeast-1 \
  --create-bucket-configuration LocationConstraint=ap-southeast-1
```

**2. Upload Files from Local to S3 (AWS CLI):**
```bash
# Upload a single file
aws s3 cp ./local-file.txt s3://my-week2-bucket/

# Sync an entire directory
aws s3 sync ./local-folder/ s3://my-week2-bucket/data/

# Verify upload
aws s3 ls s3://my-week2-bucket/
```

**3. Configure S3 Lifecycle Policies:**

| Rule | Action | Transition |
|------|--------|-----------|
| Archive infrequent data | Move to S3 Standard-IA | After **30 days** |
| Archive old data | Move to S3 Glacier Instant Retrieval | After **90 days** |
| Delete expired objects | Permanently delete | After **365 days** |
| Clean up incomplete multipart uploads | Abort | After **7 days** |

**Clean up after practice:**
```bash
# Delete all objects in the bucket first
aws s3 rm s3://my-week2-bucket/ --recursive

# Then delete the bucket itself
aws s3api delete-bucket --bucket my-week2-bucket
```

> ⚠️ Always clean up all resources after practice to avoid unexpected charges.

> **Key Takeaway:** S3 Lifecycle policies are a zero-cost automation strategy to dramatically reduce storage costs — transition data to cheaper storage classes as it ages.

---

#### Day 3 — Wednesday, 06/05/2026: CloudFormation, Data Engineering & RDS

##### Theory: AWS CloudFormation

**AWS CloudFormation** is AWS's native **Infrastructure as Code (IaC)** service — define your entire AWS environment in a declarative JSON or YAML template and provision it consistently and repeatably.

Key concepts covered:
- **Template anatomy:** `AWSTemplateFormatVersion`, `Parameters`, `Resources`, `Outputs`, `Mappings`, `Conditions`.
- **Stacks:** Logical grouping of AWS resources created from a single template; update/delete as a unit.
- **Change Sets:** Preview infrastructure changes before applying them (safe deployments).
- **Stack Sets:** Deploy stacks across multiple accounts and regions simultaneously.
- **Drift Detection:** Identify manually changed resources that diverge from the template.
- **Nested Stacks:** Modularize large templates into reusable components.

> **Key Takeaway:** CloudFormation enables **repeatable, version-controlled infrastructure** — the foundation of GitOps and CI/CD pipelines for cloud environments.

---

##### Theory: AWS Glue & Amazon Athena

**AWS Glue** is a fully managed **ETL (Extract, Transform, Load)** service for building data pipelines without managing infrastructure.

Key concepts covered for AWS Glue:
- **Data Catalog:** Central metadata repository — automatically crawls data sources (S3, RDS, DynamoDB) to discover schemas.
- **Glue Crawlers:** Automatically infer schemas and populate the Data Catalog.
- **ETL Jobs:** Spark-based (PySpark/Scala) or Python Shell scripts for data transformation.
- **Glue Studio:** Visual drag-and-drop ETL workflow builder.
- **Glue DataBrew:** No-code data profiling and cleaning for analysts.

**Amazon Athena** is a serverless, interactive **SQL query engine** for analyzing data directly in **Amazon S3** — no data loading required.

Key concepts covered for Athena:
- Supports standard **ANSI SQL**; query data in CSV, JSON, Parquet, ORC, Avro formats.
- **Pay per query:** Charged only for data scanned (optimize with columnar formats + partitioning).
- Integrates with **AWS Glue Data Catalog** as its metadata layer.
- **Federated Queries:** Query data across RDS, DynamoDB, Redshift, and on-premises sources.
- Results saved automatically to a designated **S3 output bucket**.

> **Key Takeaway:** The Glue + Athena combination creates a powerful, cost-effective **data lake analytics** stack — ingest raw data to S3, catalog with Glue, query instantly with Athena.

---

##### Hands-on: Initialize & Configure a Relational Database (RDS)

**Objective:** Provision a managed PostgreSQL (or MySQL) relational database using Amazon RDS.

**1. Create a DB Subnet Group:**
- Navigate to **RDS Console** → **Subnet Groups** → **Create DB Subnet Group**.
- Select the VPC and include at least 2 subnets across different Availability Zones (required for Multi-AZ).

**2. Configure Security Group for RDS:**
- Allow inbound `PostgreSQL (port 5432)` or `MySQL (port 3306)` from the EC2 security group (or your IP).

**3. Launch RDS Instance:**

| Parameter | Value |
|-----------|-------|
| Engine | PostgreSQL 15 (or MySQL 8.0) |
| Template | Free Tier |
| Instance class | `db.t3.micro` |
| Storage | 20 GB gp2 (General Purpose SSD) |
| Multi-AZ | Disabled (Free Tier) |
| VPC | Custom VPC (from Day 1) |
| Public Access | No |
| Backup Retention | 7 days |

**4. Connect to the Database:**
```bash
# Using psql (PostgreSQL)
psql -h <rds-endpoint> -U admin -d postgres

# Using mysql client
mysql -h <rds-endpoint> -u admin -p
```

**5. Clean up after practice:**
- Delete the RDS instance (disable final snapshot to avoid costs).
- Delete the DB Subnet Group after instance deletion completes.

> **Key Takeaway:** Amazon RDS abstracts away all database administration tasks (patching, backups, failover) — enabling developers to focus on data modeling and application logic rather than DBA work.

---

### Topics Learned This Week

| Date | Topic |
|------|-------|
| 04/5 | AWS CLI — Command Line Interface for AWS |
| 04/5 | NoSQL Databases with Amazon DynamoDB |
| 04/5 | CloudFront & Lambda@Edge |
| 05/5 | AWS Lambda — Serverless Compute |
| 05/5 | AWS CDK — Cloud Development Kit |
| 05/5 | AWS Toolkit for VS Code |
| 05/5 | Amazon EBS Data Lifecycle Manager |
| 06/5 | AWS CloudFormation — Infrastructure as Code |
| 06/5 | AWS Glue & Amazon Athena — Data Engineering |

---

### Week 2 Achievements

* **AWS CLI** mastered for scripted management of EC2, S3, IAM, and other core services.
* **Custom VPC** designed with public subnets, Internet Gateway, and Route Tables; EC2 web server successfully deployed.
* **S3 operations** automated via CLI: bucket creation, file upload/sync, and lifecycle policy configuration.
* **DynamoDB, CloudFront/Lambda@Edge, Lambda, CDK** — strong theoretical understanding established.
* **AWS Glue + Athena** data lake analytics pipeline concepts understood.
* **RDS relational database** (PostgreSQL/MySQL) successfully provisioned within a custom VPC.
* Infrastructure-as-Code fundamentals solidified with **AWS CloudFormation** and **AWS CDK**.

---

*Primary Reference: [First Cloud Journey — AWS Study Group](https://cloudjourney.awsstudygroup.com/)*
