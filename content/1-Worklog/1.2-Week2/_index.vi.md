---
title: "Worklog Tuần 2"
date: 2026-05-06
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

> **Tuần 2 — Đào sâu vào các dịch vụ AWS:** Mở rộng kỹ năng thực hành với CLI, serverless, lưu trữ, cơ sở dữ liệu, infrastructure-as-code và phân tích dữ liệu.

---

### Mục tiêu tuần 2

* Thành thạo **AWS CLI** để quản lý tài nguyên cloud bằng lập trình.
* Hiểu và áp dụng **điện toán serverless** với AWS Lambda và kiến trúc event-driven.
* Làm việc với **NoSQL** (DynamoDB), **CDN** (CloudFront) và điện toán biên (Lambda@Edge).
* Thực hành **tự động hóa hạ tầng** sử dụng AWS CDK và AWS CloudFormation.
* Khám phá quy trình **data engineering** với AWS Glue và Amazon Athena.
* Thực hành triển khai web server, quản lý S3 lifecycle, và khởi tạo cơ sở dữ liệu quan hệ.

---

### Lịch công việc tuần 2

| Thứ | Lý thuyết học | Thực hành | Ngày |
| --- | ------------- | --------- | ---- |
| **2** | AWS CLI · NoSQL với Amazon DynamoDB · CloudFront & Lambda@Edge | Deploy simple web server · Tạo EC2, VPC, Subnet cơ bản | 04/05/2026 |
| **3** | AWS Lambda · AWS CDK · AWS Toolkit for VS Code · Amazon EBS Data Lifecycle Manager | Upload file từ local lên S3 · Tạo S3 bucket · Thiết lập Lifecycle Policies | 05/05/2026 |
| **4** | AWS CloudFormation · AWS Glue & Amazon Athena | Khởi tạo và cấu hình cơ sở dữ liệu quan hệ (PostgreSQL/MySQL) | 06/05/2026 |

---

### Chi tiết công việc

#### Ngày 1 — Thứ 2, 04/05/2026: CLI, NoSQL, CDN & Edge Computing

##### Lý thuyết: AWS CLI

**AWS CLI (Command Line Interface)** là công cụ dòng lệnh thống nhất để tương tác với tất cả dịch vụ AWS trực tiếp từ terminal — cho phép tự động hóa và lập trình các quy trình cloud.

Các nội dung đã học:
- Cài đặt và cấu hình AWS CLI (`aws configure` với Access Key, Secret, Region, Output format).
- Chạy các lệnh phổ biến: `aws ec2 describe-instances`, `aws s3 ls`, `aws iam list-users`.
- Sử dụng flag `--query` và `--output` để lọc và định dạng kết quả.
- Tạo **named profiles** để quản lý đa tài khoản.

> **Bài học:** AWS CLI là công cụ không thể thiếu cho DevOps — mọi tài nguyên có thể tạo trên Console đều có thể quản lý qua CLI.

---

##### Lý thuyết: Cơ sở dữ liệu NoSQL với Amazon DynamoDB

**Amazon DynamoDB** là cơ sở dữ liệu NoSQL serverless, fully managed, cung cấp hiệu suất mili giây đơn ở mọi quy mô — lý tưởng cho các ứng dụng traffic cao.

Các nội dung đã học:
- **Mô hình dữ liệu:** Tables, Items (hàng), Attributes (cột); không cần schema cố định.
- **Primary Keys:** Partition Key (đơn giản) và Partition Key + Sort Key (kết hợp).
- **Chế độ đọc/ghi:** Provisioned (cố định) vs. On-Demand (linh hoạt).
- **DynamoDB Streams:** Ghi nhận thay đổi cấp item để xây dựng kiến trúc event-driven.
- **Global Tables:** Bảng sao chép đa vùng cho độ trễ cực thấp trên toàn cầu.
- **DAX (DynamoDB Accelerator):** Cache in-memory cho hiệu suất đọc micro giây.

> **Bài học:** DynamoDB phù hợp cho các use case cần mở rộng ngang, schema linh hoạt, và độ trễ mili giây ổn định (bảng xếp hạng game, session store, IoT).

---

##### Lý thuyết: CloudFront & Lambda@Edge

**Amazon CloudFront** là **CDN (Content Delivery Network)** phân phối toàn cầu, cache và phân phối nội dung từ các **Edge Locations** gần người dùng nhất, giảm thiểu độ trễ.

**Lambda@Edge** mở rộng AWS Lambda để chạy code tại các edge location của CloudFront — cho phép tùy chỉnh request/response mà không cần định tuyến traffic về origin.

Các nội dung đã học:
- **Distributions**, **origins** (S3, ALB, EC2, custom HTTP) và **behaviors** của CloudFront.
- **Cache policies** và **origin request policies** để kiểm soát cache chi tiết.
- Ép buộc **HTTPS** và **SSL certificate** tùy chỉnh qua AWS Certificate Manager (ACM).
- **Triggers** của Lambda@Edge: Viewer Request, Origin Request, Origin Response, Viewer Response.
- Các use case phổ biến: Viết lại URL, A/B testing, xác thực tại edge, tối ưu hóa ảnh.

---

##### Thực hành: Deploy Simple Web Server & Cấu hình EC2, VPC, Subnet

**1. Tạo VPC và Subnet:**

| Tài nguyên | Cấu hình |
|------------|----------|
| VPC | CIDR: `10.0.0.0/16` |
| Public Subnet | CIDR: `10.0.1.0/24`, AZ: `ap-southeast-1a` |
| Internet Gateway | Gắn vào VPC |
| Route Table | Route `0.0.0.0/0` → Internet Gateway |

**2. Khởi chạy EC2 Instance làm Web Server:**
1. Vào **EC2 Console** → **Launch Instance**.
2. Chọn **Amazon Linux 2023 AMI** (miễn phí với free tier).
3. Chọn loại instance: `t2.micro`.
4. Đặt instance trong VPC và public subnet vừa tạo.
5. Cấu hình **Security Group:** Cho phép inbound `HTTP (port 80)` và `SSH (port 22)`.
6. Thêm **User Data script** để tự động cài đặt và khởi động Apache:
   ```bash
   #!/bin/bash
   yum update -y
   yum install -y httpd
   systemctl start httpd
   systemctl enable httpd
   echo "<h1>Hello from AWS EC2 - Tuần 2!</h1>" > /var/www/html/index.html
   ```
7. Khởi chạy instance và truy cập public IP để xác minh web server hoạt động.

**Dọn dẹp sau thực hành:**
- **Terminate** EC2 instance (EC2 Console → Instances → Terminate instance).
- **Xóa** Internet Gateway (detach khỏi VPC trước, sau đó xóa).
- **Xóa** Route Table, Subnet, và cuối cùng là VPC.

> ⚠️ Luôn dọn dẹp toàn bộ tài nguyên sau mỗi buổi thực hành để tránh phát sinh chi phí ngoài mong muốn.

> **Bài học:** Hiểu rõ networking VPC (subnets, route tables, Internet Gateways) là nền tảng để triển khai bất kỳ tài nguyên nào có thể truy cập internet trên AWS.

---

#### Ngày 2 — Thứ 3, 05/05/2026: Serverless, IaC & Quản lý lưu trữ

##### Lý thuyết: AWS Lambda

**AWS Lambda** là dịch vụ compute serverless, event-driven — chạy code phản ứng với các sự kiện mà không cần provisioning hay quản lý server.

Các nội dung đã học:
- **Mô hình thực thi:** Function → Handler → Runtime (Node.js, Python, Java, Go,...).
- **Triggers:** API Gateway, S3 events, DynamoDB Streams, SQS, CloudWatch Events, SNS.
- **Concurrency:** Reserved concurrency vs. Provisioned concurrency.
- **Layers:** Đóng gói thư viện/dependencies dùng chung để giữ code function gọn gàng.
- **Environment Variables** và tích hợp **Secrets Manager** để cấu hình bảo mật.
- **Lambda URLs:** Endpoint HTTPS trực tiếp không cần API Gateway.
- Giá: Tính theo số request + thời gian thực thi (RAM 128 MB–10 GB, timeout tối đa 15 phút).

> **Bài học:** Mô hình event-driven của Lambda là xương sống của các kiến trúc serverless hiện đại trên AWS — tích hợp sâu với hầu hết mọi dịch vụ AWS.

---

##### Lý thuyết: AWS CDK (Cloud Development Kit)

**AWS CDK** cho phép định nghĩa hạ tầng cloud bằng ngôn ngữ lập trình quen thuộc (TypeScript, Python, Java, C#) — biên dịch thành CloudFormation templates bên dưới.

Các nội dung đã học:
- **Constructs:** Các thành phần cloud tái sử dụng (L1: CFN thuần, L2: có sẵn, L3: pattern cao cấp).
- **Stacks:** Đơn vị deployment, ánh xạ 1:1 với CloudFormation stacks.
- **Apps:** Chương trình CDK gốc chứa một hoặc nhiều stacks.
- Quy trình: `cdk init` → Định nghĩa constructs → `cdk synth` → `cdk deploy`.
- Ưu điểm so với CloudFormation thuần: Type safety, IDE autocomplete, logic/vòng lặp/điều kiện.

---

##### Lý thuyết: AWS Toolkit for VS Code

**AWS Toolkit for VS Code** là extension IDE cho phép tương tác với dịch vụ AWS trực tiếp từ VS Code.

Các tính năng đã khám phá:
- Duyệt và gọi **Lambda functions** mà không cần rời editor.
- Quản lý **S3 buckets và objects** qua panel Explorer.
- Hỗ trợ template **CloudFormation** và **CDK** với kiểm tra cú pháp.
- Debug Lambda functions cục bộ tích hợp **SAM CLI**.
- Quản lý credentials qua **AWS Profiles**.

---

##### Lý thuyết: Amazon EBS Data Lifecycle Manager

**Amazon EBS Data Lifecycle Manager (DLM)** tự động hóa việc tạo, lưu giữ và xóa **EBS Snapshots** — cơ chế backup cho EBS volumes của EC2.

Các nội dung đã học:
- **Lifecycle policies:** Lên lịch tạo snapshot (theo giờ, ngày, tuần).
- **Retention rules:** Giữ N snapshots mới nhất hoặc giữ trong N ngày.
- **Cross-region copy:** Tự động sao chép snapshot sang vùng disaster recovery.
- **Fast Snapshot Restore (FSR):** Pre-warm snapshots để khôi phục volume ngay lập tức với hiệu năng đầy đủ.

> **Bài học:** DLM là chiến lược backup "set it and forget it" cho EBS — luôn cấu hình DLM policies trong môi trường production để đảm bảo độ bền dữ liệu.

---

##### Thực hành: S3 — Upload Files, Tạo Bucket & Thiết lập Lifecycle Policies

**1. Tạo S3 Bucket:**
```bash
aws s3api create-bucket \
  --bucket my-week2-bucket-$(date +%s) \
  --region ap-southeast-1 \
  --create-bucket-configuration LocationConstraint=ap-southeast-1
```

**2. Upload File từ Local lên S3 (AWS CLI):**
```bash
# Upload một file đơn lẻ
aws s3 cp ./local-file.txt s3://my-week2-bucket/

# Sync toàn bộ thư mục
aws s3 sync ./local-folder/ s3://my-week2-bucket/data/

# Kiểm tra sau khi upload
aws s3 ls s3://my-week2-bucket/
```

**3. Cấu hình S3 Lifecycle Policies:**

| Quy tắc | Hành động | Thời điểm áp dụng |
|---------|-----------|-------------------|
| Lưu trữ dữ liệu ít dùng | Chuyển sang S3 Standard-IA | Sau **30 ngày** |
| Lưu trữ dữ liệu cũ | Chuyển sang S3 Glacier Instant Retrieval | Sau **90 ngày** |
| Xóa object hết hạn | Xóa vĩnh viễn | Sau **365 ngày** |
| Dọn dẹp multipart upload dang dở | Hủy bỏ | Sau **7 ngày** |

**Dọn dẹp sau thực hành:**
```bash
# Xóa toàn bộ objects trong bucket trước
aws s3 rm s3://my-week2-bucket/ --recursive

# Sau đó xóa bucket
aws s3api delete-bucket --bucket my-week2-bucket
```

> ⚠️ Luôn dọn dẹp toàn bộ tài nguyên sau mỗi buổi thực hành để tránh phát sinh chi phí ngoài mong muốn.

> **Bài học:** S3 Lifecycle policies là chiến lược tự động hóa không tốn chi phí để giảm đáng kể chi phí lưu trữ — chuyển dữ liệu sang storage class rẻ hơn khi dữ liệu cũ dần.

---

#### Ngày 3 — Thứ 4, 06/05/2026: CloudFormation, Data Engineering & RDS

##### Lý thuyết: AWS CloudFormation

**AWS CloudFormation** là dịch vụ **Infrastructure as Code (IaC)** gốc của AWS — định nghĩa toàn bộ môi trường AWS trong một template JSON hoặc YAML, triển khai nhất quán và có thể lặp lại.

Các nội dung đã học:
- **Cấu trúc template:** `AWSTemplateFormatVersion`, `Parameters`, `Resources`, `Outputs`, `Mappings`, `Conditions`.
- **Stacks:** Nhóm logic các tài nguyên AWS từ một template; update/delete theo đơn vị.
- **Change Sets:** Xem trước thay đổi hạ tầng trước khi áp dụng (triển khai an toàn).
- **Stack Sets:** Triển khai stacks trên nhiều tài khoản và regions cùng lúc.
- **Drift Detection:** Phát hiện tài nguyên bị thay đổi thủ công khác với template.
- **Nested Stacks:** Modular hóa template lớn thành các thành phần tái sử dụng.

> **Bài học:** CloudFormation tạo ra **hạ tầng có thể lặp lại và kiểm soát version** — nền tảng của GitOps và CI/CD pipelines cho môi trường cloud.

---

##### Lý thuyết: AWS Glue & Amazon Athena

**AWS Glue** là dịch vụ **ETL (Extract, Transform, Load)** fully managed để xây dựng data pipelines mà không cần quản lý hạ tầng.

Các nội dung đã học về AWS Glue:
- **Data Catalog:** Kho metadata trung tâm — tự động crawl các data sources (S3, RDS, DynamoDB) để phát hiện schema.
- **Glue Crawlers:** Tự động suy luận schema và cập nhật Data Catalog.
- **ETL Jobs:** Script PySpark/Scala hoặc Python Shell để transform dữ liệu.
- **Glue Studio:** Công cụ xây dựng quy trình ETL trực quan (kéo thả).
- **Glue DataBrew:** Profiling và làm sạch dữ liệu không cần code dành cho analysts.

**Amazon Athena** là engine **truy vấn SQL serverless, tương tác** để phân tích dữ liệu trực tiếp trên **Amazon S3** — không cần tải dữ liệu.

Các nội dung đã học về Athena:
- Hỗ trợ **ANSI SQL** chuẩn; truy vấn dữ liệu định dạng CSV, JSON, Parquet, ORC, Avro.
- **Tính tiền theo query:** Chỉ tính phí dữ liệu được quét (tối ưu bằng columnar formats + partitioning).
- Tích hợp với **AWS Glue Data Catalog** làm lớp metadata.
- **Federated Queries:** Truy vấn dữ liệu trên RDS, DynamoDB, Redshift và nguồn on-premises.
- Kết quả tự động lưu vào **S3 output bucket** được chỉ định.

> **Bài học:** Bộ đôi Glue + Athena tạo ra stack **phân tích data lake** hiệu quả, tiết kiệm chi phí — ingest dữ liệu thô vào S3, catalog bằng Glue, truy vấn ngay bằng Athena.

---

##### Thực hành: Khởi tạo & Cấu hình Cơ sở dữ liệu Quan hệ (RDS)

**Mục tiêu:** Provisioning cơ sở dữ liệu PostgreSQL (hoặc MySQL) được quản lý bằng Amazon RDS.

**1. Tạo DB Subnet Group:**
- Vào **RDS Console** → **Subnet Groups** → **Create DB Subnet Group**.
- Chọn VPC và ít nhất 2 subnets ở các Availability Zones khác nhau (bắt buộc cho Multi-AZ).

**2. Cấu hình Security Group cho RDS:**
- Cho phép inbound `PostgreSQL (port 5432)` hoặc `MySQL (port 3306)` từ security group của EC2 (hoặc IP của bạn).

**3. Khởi chạy RDS Instance:**

| Tham số | Giá trị |
|---------|---------|
| Engine | PostgreSQL 15 (hoặc MySQL 8.0) |
| Template | Free Tier |
| Instance class | `db.t3.micro` |
| Storage | 20 GB gp2 (General Purpose SSD) |
| Multi-AZ | Tắt (Free Tier) |
| VPC | Custom VPC (từ Ngày 1) |
| Public Access | Không |
| Backup Retention | 7 ngày |

**4. Kết nối đến cơ sở dữ liệu:**
```bash
# Dùng psql (PostgreSQL)
psql -h <rds-endpoint> -U admin -d postgres

# Dùng mysql client
mysql -h <rds-endpoint> -u admin -p
```

**5. Dọn dẹp sau thực hành:**
- Xóa RDS instance (tắt final snapshot để tránh chi phí).
- Xóa DB Subnet Group sau khi instance đã xóa hoàn toàn.

> **Bài học:** Amazon RDS loại bỏ tất cả các tác vụ quản trị cơ sở dữ liệu (patching, backup, failover) — cho phép developer tập trung vào data modeling và logic ứng dụng thay vì công việc DBA.

---

### Nội dung đã học trong tuần

| Ngày | Chủ đề |
|------|--------|
| 04/5 | AWS CLI — Giao diện dòng lệnh cho AWS |
| 04/5 | Cơ sở dữ liệu NoSQL với Amazon DynamoDB |
| 04/5 | CloudFront & Lambda@Edge |
| 05/5 | AWS Lambda — Serverless Compute |
| 05/5 | AWS CDK — Cloud Development Kit |
| 05/5 | AWS Toolkit for VS Code |
| 05/5 | Amazon EBS Data Lifecycle Manager |
| 06/5 | AWS CloudFormation — Infrastructure as Code |
| 06/5 | AWS Glue & Amazon Athena — Data Engineering |

---

### Kết quả đạt được tuần 2

* **AWS CLI** thành thạo để quản lý EC2, S3, IAM và các dịch vụ cốt lõi bằng script.
* **Custom VPC** thiết kế với public subnets, Internet Gateway và Route Tables; web server EC2 triển khai thành công.
* **Tự động hóa S3** qua CLI: tạo bucket, upload/sync files và cấu hình lifecycle policies.
* **DynamoDB, CloudFront/Lambda@Edge, Lambda, CDK** — hiểu vững lý thuyết.
* Nắm được pipeline phân tích data lake với **AWS Glue + Athena**.
* **Cơ sở dữ liệu quan hệ RDS** (PostgreSQL/MySQL) khởi tạo thành công trong custom VPC.
* Củng cố nền tảng Infrastructure-as-Code với **AWS CloudFormation** và **AWS CDK**.

---

*Nguồn tài liệu chính: [First Cloud Journey — AWS Study Group](https://cloudjourney.awsstudygroup.com/)*
