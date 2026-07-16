---
title: "Tuần 4"
date: 2026-05-11
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

Mục tiêu tuần:
- Học sâu về AWS CloudFormation để tự động hóa và quản lý hạ tầng.
- Hiểu các thành phần AWS Glue: Data Catalog, Crawlers và ETL jobs.
- Sử dụng Amazon Athena để truy vấn tập dữ liệu trên S3 bằng SQL serverless.
- Áp dụng các phương pháp bảo mật tốt nhất cho mạng VPC.

Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày |
|---|---|---|
| Thứ Hai | Nghiên cứu các stack lồng nhau, stack sets, change sets và drift detection trong CloudFormation. | 11/5 |
| Thứ Ba | Cấu hình các Glue Crawler để nhận diện tự động schema dữ liệu trên S3 và xây dựng Data Catalog. | 12/5 |
| Thứ Tư | Chạy các truy vấn SQL serverless bằng Amazon Athena và thiết lập cấu hình Athena Workgroups. | 13/5 |
| Thứ Năm | Triển khai các instance Amazon RDS PostgreSQL trong VPC với liên kết bảo mật security group. | 14/5 |
| Thứ Sáu | Thiết lập cấu hình VPC flow logs, Network Access Control Lists và các endpoint PrivateLink. | 15/5 |

Kết quả đạt được trong tuần là gì:
- Xây dựng thành công các template tự động hóa hạ tầng có khả năng tái sử dụng bằng CloudFormation.
- Tự động hóa việc tạo schema dữ liệu thông qua AWS Glue Crawlers.
- Kiểm soát chi phí truy vấn dữ liệu hiệu quả bằng cách thiết lập giới hạn cho Athena workgroups.
- Tăng cường bảo mật mạng VPC bằng việc thiết lập các liên kết security group phân cấp và chặt chẽ cho cơ sở dữ liệu.
