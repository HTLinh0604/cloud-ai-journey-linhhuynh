---
title: "Tổng quan"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 5.1 </b> "
---

# Tổng quan Workshop

## Workshop này về gì?

Workshop này hướng dẫn bạn xây dựng một **FinOps-Optimized Serverless Medallion Data Lakehouse** trên AWS - một nền tảng phân tích dữ liệu cấp production được thiết kế cho bài toán phân tích hành vi khách hàng thương mại điện tử.

Ý tưởng cốt lõi là chứng minh cách các doanh nghiệp thương mại điện tử hiện đại có thể thu được **insights phân tích sâu** (xu hướng doanh thu, phân khúc khách hàng, tỉ lệ chuyển đổi phễu) từ hai nguồn dữ liệu:

1. **Sự kiện clickstream thời gian thực** từ ứng dụng web và mobile (luồng streaming)
2. **Bản ghi đơn hàng giao dịch** từ cơ sở dữ liệu thương mại điện tử (luồng batch)

...trong khi giữ hạ tầng **100% serverless** và hóa đơn hàng tháng dưới **$10/tháng**.

---

## Bối cảnh kinh doanh

Hãy tưởng tượng bạn là kỹ sư dữ liệu tại một công ty thương mại điện tử đang phát triển. Các bên liên quan kinh doanh hỏi:

- *"Danh mục sản phẩm nào tạo ra nhiều doanh thu nhất?"*
- *"Tỉ lệ chuyển đổi phễu bán hàng từ xem sản phẩm đến mua hàng là bao nhiêu?"*
- *"Quốc gia nào tạo ra doanh thu cao nhất? Loại thiết bị nào?"*
- *"Xu hướng doanh thu của chúng ta trong năm qua như thế nào?"*

Không có nền tảng dữ liệu phù hợp, việc trả lời những câu hỏi này đòi hỏi xuất CSV thủ công, chạy SQL ad-hoc trực tiếp lên cơ sở dữ liệu production, hoặc xây dựng các cluster data warehouse luôn chạy tốn kém.

Workshop này xây dựng nền tảng trả lời tất cả những câu hỏi đó - tự động, đáng tin cậy và tiết kiệm chi phí - sử dụng các dịch vụ AWS managed.

---

## Kết quả học tập

Sau khi hoàn thành workshop này, bạn sẽ có khả năng:

| Kỹ năng | Những gì bạn sẽ học |
|---------|-------------------|
| **VPC & Mạng** | Tạo VPC, Subnets, Internet Gateway, Route Tables, Security Groups cho nền tảng dữ liệu an toàn |
| **S3 Data Lake** | Thiết kế cấu trúc S3 nhiều tầng (Raw → Bronze → Silver → Gold) với bucket policies phù hợp |
| **AWS Glue ETL** | Viết PySpark ETL jobs chuyển đổi dữ liệu qua các tầng Medallion |
| **Glue Data Catalog** | Đăng ký schemas bảng theo chương trình - không cần crawlers thủ công |
| **Amazon Athena** | Chạy SQL queries serverless trên dữ liệu S3 sử dụng Data Catalog |
| **Streamlit trên EC2** | Deploy Python web dashboard trên EC2 trong VPC |
| **CloudWatch Monitoring** | Thiết lập alarms và dashboard để quan sát pipeline |
| **IAM Security** | Áp dụng IAM roles quyền tối thiểu cho từng dịch vụ |
| **FinOps** | Hiểu cách Parquet, phân vùng và caching giảm chi phí Athena 85–90% |

---

## Tóm tắt kiến trúc

Nền tảng được xây dựng qua **6 lớp chức năng**:

```
┌─────────────────────────────────────────────────────────┐
│  NGUỒN DỮ LIỆU                                          │
│  • Website/Mobile → sự kiện JSON thời gian thực         │
│  • DB thương mại điện tử → batch CSV xuất định kỳ      │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│  LỚP INGESTION                                          │
│  • API Gateway → Firehose → Lambda → S3 (streaming)    │
│  • EventBridge → Lambda (trích xuất DB) → S3 (batch)  │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│  LỚP LƯU TRỮ - KIẾN TRÚC MEDALLION                    │
│  S3: Raw → Bronze (Parquet) → Silver (sạch) → Gold    │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│  LỚP XỬ LÝ                                             │
│  • Glue ETL Job 1: Raw → Bronze (CSV sang Parquet)     │
│  • Glue ETL Job 2: Bronze → Silver (làm sạch/dedup)   │
│  • Glue ETL Job 3: Silver → Gold (tổng hợp KPI)       │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│  LỚP TRUY VẤN                                          │
│  • Glue Data Catalog (kho siêu dữ liệu)               │
│  • Amazon Athena (SQL serverless trên S3)              │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│  LỚP TRỰC QUAN HÓA                                     │
│  • Streamlit Dashboard trên EC2 (trong VPC)            │
│  • Kết nối Athena qua aws-wrangler + boto3             │
└─────────────────────────────────────────────────────────┘
```

---

## Dịch vụ AWS sử dụng

| Dịch vụ | Vai trò trong Workshop |
|---------|----------------------|
| **Amazon VPC** | Mạng cách ly cho EC2 và nền tảng dữ liệu |
| **Amazon Subnet** | Public subnet cho EC2 Dashboard |
| **Internet Gateway** | Cho phép truy cập internet cho EC2 |
| **Route Table** | Định tuyến traffic từ subnet đến Internet Gateway |
| **Security Group** | Cho phép inbound port 8501 (Streamlit) + SSH |
| **Amazon S3** | Data lake bốn tầng (Raw, Bronze, Silver, Gold) |
| **Amazon Data Firehose** | Đệm và phân phối sự kiện streaming vào S3 |
| **Amazon API Gateway** | HTTP endpoint để tiếp nhận sự kiện client |
| **AWS Lambda** | Chuyển đổi Firehose nội tuyến + trích xuất DB |
| **Amazon EventBridge Scheduler** | Trigger Lambda batch theo lịch |
| **AWS Glue** | PySpark ETL jobs để chuyển đổi dữ liệu |
| **AWS Glue Data Catalog** | Kho siêu dữ liệu cho bảng Athena |
| **Amazon Athena** | SQL queries serverless trên S3 Gold layer |
| **Amazon EC2** | Host Streamlit dashboard |
| **Amazon EBS** | Lưu trữ liên tục cho EC2 instance |
| **Elastic IP** | IP tĩnh cho EC2 instance |
| **AWS IAM** | Roles quyền tối thiểu theo từng dịch vụ |
| **Amazon CloudWatch** | Logs, metrics và alarms |
| **AWS KMS** | Mã hóa khi lưu trữ cho S3 buckets |

---

## Source Code

Tất cả source code trong workshop có trong thư mục `source_code/`:

| File | Mô tả |
|------|-------|
| `raw_to_bronze_job.py` | Glue ETL Job 1: Đọc CSV + JSON streaming từ Raw, ghi Parquet vào Bronze |
| `bronze_to_silver_job.py` | Glue ETL Job 2: Loại bỏ trùng, làm sạch, chuẩn hóa → Silver |
| `silver_to_gold_job.py` | Glue ETL Job 3: Tổng hợp KPI nghiệp vụ → Gold; đăng ký bảng Glue Catalog |
| `athena_create_tables.sql` | Câu lệnh SQL tạo external tables trong Athena |
| `athena_queries.sql` | Mẫu truy vấn nghiệp vụ để chạy trên Gold layer |
| `app_beautiful.py` | Ứng dụng Streamlit dashboard kết nối Athena qua aws-wrangler |
