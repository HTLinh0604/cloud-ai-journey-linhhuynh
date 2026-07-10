---
title: "Dọn dẹp tài nguyên"
date: 2024-01-01
weight: 5
chapter: false
pre: " <b> 5.5 </b> "
---

# Dọn dẹp tài nguyên

Sau khi hoàn thành workshop, việc **xóa toàn bộ tài nguyên AWS** là cực kỳ quan trọng để tránh phát sinh chi phí liên tục. Thực hiện theo checklist sau theo đúng thứ tự - một số tài nguyên phụ thuộc vào tài nguyên khác phải được xóa trước.

> ⚠️ **Quan trọng:** Bỏ qua bước dọn dẹp sẽ dẫn đến chi phí liên tục. EC2 instances, Elastic IPs và Glue ETL jobs còn hoạt động sẽ tiếp tục tính phí tài khoản của bạn.

**Thời gian ước tính:** 15–20 phút

---

## Checklist dọn dẹp

### Bước 1: Dừng và Xóa EC2 Instance

**AWS Console → EC2 → Instances → Chọn `lakehouse-dashboard`**
- **Instance state → Terminate instance** → Xác nhận

```bash
aws ec2 terminate-instances --instance-ids <your-instance-id>

# Xác minh đã xóa
aws ec2 describe-instances --instance-ids <your-instance-id> \
    --query "Reservations[0].Instances[0].State.Name"
# Kết quả mong đợi: "terminated"
```

---

### Bước 2: Giải phóng Elastic IP

**AWS Console → EC2 → Elastic IPs → Chọn IP → Actions → Release Elastic IP address**

> ⚠️ Elastic IP được phân bổ nhưng không gắn với instance đang chạy sẽ bị tính phí **$0.005/giờ** (~$3.60/tháng). Giải phóng ngay sau khi xóa EC2.

```bash
aws ec2 describe-addresses --query "Addresses[*].{IP:PublicIp,AllocId:AllocationId}"
aws ec2 release-address --allocation-id <allocation-id>
```

---

### Bước 3: Xóa Glue ETL Jobs

**AWS Console → AWS Glue → ETL Jobs → Chọn tất cả 3 job → Actions → Delete**

```bash
aws glue delete-job --job-name raw-to-bronze-job
aws glue delete-job --job-name bronze-to-silver-job
aws glue delete-job --job-name silver-to-gold-job
```

---

### Bước 4: Xóa Glue Data Catalog

```bash
# Xóa các bảng
for table in event_summary daily_revenue payment_summary country_revenue device_summary source_summary dashboard_summary; do
    aws glue delete-table --database-name customer_behavior_catalog_db --name $table
    echo "Đã xóa bảng: $table"
done

# Xóa database
aws glue delete-database --name customer_behavior_catalog_db
```

---

### Bước 5: Xóa S3 Bucket

```bash
# Xóa tất cả objects
aws s3 rm s3://customer-behavior-lakehouse1 --recursive

# Xóa bucket
aws s3 rb s3://customer-behavior-lakehouse1 --force
```

---

### Bước 6: Xóa CloudWatch Alarms và Dashboard

```bash
aws cloudwatch delete-alarms \
    --alarm-names "GlueJobFailure-Alert" "Athena-DataScan-Alert" "EC2-CPU-High-Alert"

aws cloudwatch delete-dashboards --dashboard-names "lakehouse-pipeline-health"

# Xóa Log Groups
aws logs delete-log-group --log-group-name /aws-glue/jobs/output
aws logs delete-log-group --log-group-name /aws-glue/jobs/error
```

---

### Bước 7: Xóa VPC và các tài nguyên mạng

```bash
# 1. Xóa Security Group
aws ec2 delete-security-group --group-name lakehouse-ec2-sg

# 2. Xóa Internet Gateway (detach trước)
IGW_ID=$(aws ec2 describe-internet-gateways \
    --filters "Name=tag:Name,Values=lakehouse-igw" \
    --query "InternetGateways[0].InternetGatewayId" --output text)
VPC_ID=$(aws ec2 describe-vpcs \
    --filters "Name=tag:Name,Values=lakehouse-vpc" \
    --query "Vpcs[0].VpcId" --output text)
aws ec2 detach-internet-gateway --internet-gateway-id $IGW_ID --vpc-id $VPC_ID
aws ec2 delete-internet-gateway --internet-gateway-id $IGW_ID

# 3. Xóa Subnet
SUBNET_ID=$(aws ec2 describe-subnets \
    --filters "Name=tag:Name,Values=lakehouse-public-subnet" \
    --query "Subnets[0].SubnetId" --output text)
aws ec2 delete-subnet --subnet-id $SUBNET_ID

# 4. Xóa VPC
aws ec2 delete-vpc --vpc-id $VPC_ID
```

---

### Bước 8: Xóa IAM Roles

```bash
# Xóa Glue role
aws iam detach-role-policy --role-name AWSGlueServiceRole-lakehouse \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole
aws iam detach-role-policy --role-name AWSGlueServiceRole-lakehouse \
    --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
aws iam delete-role --role-name AWSGlueServiceRole-lakehouse

# Xóa EC2 role
aws iam detach-role-policy --role-name lakehouse-ec2-role \
    --policy-arn arn:aws:iam::aws:policy/AmazonAthenaFullAccess
aws iam detach-role-policy --role-name lakehouse-ec2-role \
    --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
aws iam delete-role --role-name lakehouse-ec2-role
```

---

### Bước 9: Xóa SNS Topic và Firehose

```bash
# Xóa SNS Topic
SNS_ARN=$(aws sns list-topics --query "Topics[?contains(TopicArn,'lakehouse')].TopicArn" --output text)
aws sns delete-topic --topic-arn $SNS_ARN

# Xóa Firehose (nếu đã tạo)
aws firehose delete-delivery-stream --delivery-stream-name lakehouse-event-stream
```

---

## Checklist tóm tắt

- [ ] EC2 instance đã bị terminate
- [ ] Elastic IP đã được giải phóng
- [ ] 3 Glue ETL jobs đã xóa
- [ ] 7 Glue Catalog tables đã xóa
- [ ] Glue database đã xóa
- [ ] S3 bucket đã làm trống và xóa
- [ ] CloudWatch alarms đã xóa
- [ ] CloudWatch dashboard đã xóa
- [ ] CloudWatch log groups đã xóa
- [ ] VPC, Subnet, IGW, Route Table, Security Group đã xóa
- [ ] IAM roles (Glue + EC2) đã xóa
- [ ] SNS topic đã xóa
- [ ] Firehose stream đã xóa (nếu có tạo)

✅ **Workshop hoàn thành!** Tất cả tài nguyên đã được dọn dẹp. Không còn phát sinh thêm chi phí nào.
