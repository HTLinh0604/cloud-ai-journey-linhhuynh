---
title: "Điều kiện tiên quyết"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 5.2 </b> "
---

# Điều kiện tiên quyết

Trước khi bắt đầu workshop, hãy đảm bảo bạn đã chuẩn bị các yếu tố sau.

---

## 1. Tài khoản AWS

- Một **tài khoản AWS** đang hoạt động với billing được bật
- Khuyến nghị: Tạo IAM user riêng thay vì dùng tài khoản root
- **AWS Region**: Sử dụng `us-east-1` (N. Virginia) xuyên suốt workshop này để đảm bảo nhất quán

> 💡 **Mẹo:** Nếu bạn đang dùng tài khoản AWS promotional credit (như từ FCAJ), hãy kiểm tra số dư credit còn lại trước khi bắt đầu.

---

## 2. Quyền IAM cần thiết

IAM user hoặc role của bạn phải có quyền cho các dịch vụ sau. Để đơn giản trong workshop này, bạn có thể gán các AWS managed policies sau:

| AWS Managed Policy | Dịch vụ được bao phủ |
|-------------------|---------------------|
| `AmazonS3FullAccess` | Tạo S3 bucket, đọc/ghi |
| `AWSGlueConsoleFullAccess` | Glue ETL jobs, Data Catalog |
| `AmazonAthenaFullAccess` | Thực thi truy vấn Athena |
| `AmazonEC2FullAccess` | EC2, VPC, Security Groups, Elastic IP |
| `AWSLambda_FullAccess` | Tạo Lambda function |
| `AmazonAPIGatewayAdministrator` | Cấu hình API Gateway |
| `CloudWatchFullAccess` | Logs, metrics, alarms |
| `AWSKeyManagementServicePowerUser` | Tạo và sử dụng KMS key |
| `IAMFullAccess` | Tạo IAM roles cho các dịch vụ |

> ⚠️ **Lưu ý:** Trong môi trường production, bạn nên áp dụng các policy quyền tối thiểu thay vì full access. Phần trên chỉ để thuận tiện trong workshop.

---

## 3. Công cụ & Phần mềm

### AWS CLI

Cài đặt và cấu hình AWS CLI v2:

```bash
# Kiểm tra cài đặt
aws --version
# Kết quả mong đợi: aws-cli/2.x.x

# Cấu hình credentials
aws configure
# Nhập: AWS Access Key ID, Secret Access Key, Region (us-east-1), Output format (json)
```

### Python 3.9+

```bash
python --version
# Kết quả mong đợi: Python 3.9.x trở lên
```

### Các Python packages cần thiết:

```bash
pip install boto3 pandas streamlit plotly awswrangler pyathena
```

---

## 4. Dữ liệu mẫu

Workshop này sử dụng dữ liệu thương mại điện tử tổng hợp. Tạo các file CSV sau để upload lên S3:

| File | Các cột | Mô tả |
|------|---------|-------|
| `customers.csv` | customer_id, name, email, country, signup_date | Dữ liệu khách hàng |
| `orders.csv` | order_id, customer_id, total_usd, payment_method, device, source, country, order_time | Giao dịch đơn hàng |
| `products.csv` | product_id, name, category, price_usd | Danh mục sản phẩm |
| `order_items.csv` | item_id, order_id, product_id, quantity, price_usd | Chi tiết đơn hàng |
| `reviews.csv` | review_id, order_id, rating, comment, review_date | Đánh giá khách hàng |
| `sessions.csv` | session_id, customer_id, start_time, end_time, device, source | Dữ liệu phiên web/app |

Bạn có thể tạo dữ liệu tổng hợp bằng Python:

```python
import pandas as pd
import random
from datetime import datetime, timedelta

orders = []
for i in range(10000):
    orders.append({
        'order_id': f'ORD-{i:05d}',
        'customer_id': f'CUST-{random.randint(1, 2000):04d}',
        'total_usd': round(random.uniform(10, 500), 2),
        'payment_method': random.choice(['credit_card', 'paypal', 'bank_transfer']),
        'device': random.choice(['mobile', 'desktop', 'tablet']),
        'source': random.choice(['organic', 'social', 'email', 'paid_ads']),
        'country': random.choice(['US', 'UK', 'DE', 'FR', 'JP', 'VN', 'SG']),
        'order_time': (datetime(2025, 1, 1) + timedelta(days=random.randint(0, 365))).isoformat()
    })

pd.DataFrame(orders).to_csv('orders.csv', index=False)
print("Đã tạo orders.csv với 10.000 bản ghi")
```

---

## 5. Checklist trước khi bắt đầu

Trước khi chuyển sang Bước 1, xác nhận:

- [ ] Tài khoản AWS đang hoạt động với billing được bật
- [ ] IAM user/role có đủ quyền như liệt kê ở trên
- [ ] AWS CLI v2 đã cài đặt và cấu hình (`aws sts get-caller-identity` trả về account ID của bạn)
- [ ] Python 3.9+ đã cài đặt
- [ ] Dữ liệu CSV mẫu đã sẵn sàng
- [ ] AWS Region đã được đặt thành `us-east-1`
