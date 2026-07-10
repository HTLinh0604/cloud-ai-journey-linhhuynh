---
title: "Clean-up"
date: 2024-01-01
weight: 5
chapter: false
pre: " <b> 5.5 </b> "
---

# Clean-up Resources

After completing the workshop, it is **critical** to delete all AWS resources to avoid ongoing charges. Follow this checklist in order - some resources depend on others being deleted first.

> ⚠️ **Important:** Skipping clean-up will result in ongoing charges. EC2 instances, Elastic IPs, and Glue ETL jobs that remain active will continue to bill your account.

**Estimated time:** 15–20 minutes

---

## Clean-up Checklist

### Step 1: Stop and Terminate EC2 Instance

**AWS Console → EC2 → Instances → Select `lakehouse-dashboard`**
- **Instance state → Terminate instance** → Confirm

> ⚠️ **Note:** Terminating deletes the EBS volume. If you want to preserve your dashboard code, SCP the files to your local machine first.

```bash
# CLI alternative
aws ec2 terminate-instances --instance-ids <your-instance-id>

# Verify termination
aws ec2 describe-instances --instance-ids <your-instance-id> \
    --query "Reservations[0].Instances[0].State.Name"
# Expected: "terminated"
```

---

### Step 2: Release Elastic IP

**AWS Console → EC2 → Elastic IPs → Select the IP → Actions → Release Elastic IP address**

> ⚠️ Elastic IPs that are allocated but not associated with a running instance are charged **$0.005/hour** (~$3.60/month). Release immediately after terminating the EC2 instance.

```bash
# CLI: first find the allocation ID
aws ec2 describe-addresses --query "Addresses[*].{IP:PublicIp,AllocId:AllocationId}"

# Release it
aws ec2 release-address --allocation-id <allocation-id>
```

---

### Step 3: Delete Glue ETL Jobs

**AWS Console → AWS Glue → ETL Jobs**

Select all three jobs → **Actions → Delete** → Confirm:
- `raw-to-bronze-job`
- `bronze-to-silver-job`
- `silver-to-gold-job`

```bash
aws glue delete-job --job-name raw-to-bronze-job
aws glue delete-job --job-name bronze-to-silver-job
aws glue delete-job --job-name silver-to-gold-job
```

---

### Step 4: Delete Glue Data Catalog Tables and Database

**Delete tables first:**
```bash
# Delete all Gold tables
for table in event_summary daily_revenue payment_summary country_revenue device_summary source_summary dashboard_summary; do
    aws glue delete-table --database-name customer_behavior_catalog_db --name $table
    echo "Deleted table: $table"
done
```

**Then delete the database:**
```bash
aws glue delete-database --name customer_behavior_catalog_db
```

---

### Step 5: Empty and Delete S3 Bucket

S3 buckets cannot be deleted unless they are empty first.

```bash
# Delete all objects (including versioned objects)
aws s3 rm s3://customer-behavior-lakehouse1 --recursive

# If versioning is enabled, also delete all versions
aws s3api delete-objects \
    --bucket customer-behavior-lakehouse1 \
    --delete "$(aws s3api list-object-versions \
        --bucket customer-behavior-lakehouse1 \
        --query '{Objects: Versions[].{Key:Key,VersionId:VersionId}}' \
        --output json)"

# Now delete the bucket
aws s3 rb s3://customer-behavior-lakehouse1 --force
```

> 📌 **Tip:** If the bucket has many versioned objects, use the S3 Console instead:
> S3 → Select bucket → **Empty** → type "permanently delete" → **Empty**
> Then: **Delete** → type bucket name → **Delete bucket**

---

### Step 6: Delete CloudWatch Alarms and Dashboard

```bash
# Delete alarms
aws cloudwatch delete-alarms \
    --alarm-names "GlueJobFailure-Alert" "Athena-DataScan-Alert" "EC2-CPU-High-Alert"

# Delete CloudWatch dashboard
aws cloudwatch delete-dashboards --dashboard-names "lakehouse-pipeline-health"
```

Delete Log Groups:
```bash
# Delete Glue job logs
aws logs delete-log-group --log-group-name /aws-glue/jobs/output
aws logs delete-log-group --log-group-name /aws-glue/jobs/error

# Delete Lambda logs (if created)
aws logs delete-log-group --log-group-name /aws/lambda/firehose-transform
```

---

### Step 7: Delete VPC and Networking Resources

Delete in this order (dependencies must be removed first):

```bash
# 1. Delete Security Group
aws ec2 delete-security-group --group-name lakehouse-ec2-sg

# 2. Delete the custom Route Table association and route table
# (Find route table ID first)
RT_ID=$(aws ec2 describe-route-tables \
    --filters "Name=tag:Name,Values=lakehouse-rt" \
    --query "RouteTables[0].RouteTableId" --output text)
aws ec2 delete-route-table --route-table-id $RT_ID

# 3. Detach and delete Internet Gateway
IGW_ID=$(aws ec2 describe-internet-gateways \
    --filters "Name=tag:Name,Values=lakehouse-igw" \
    --query "InternetGateways[0].InternetGatewayId" --output text)
VPC_ID=$(aws ec2 describe-vpcs \
    --filters "Name=tag:Name,Values=lakehouse-vpc" \
    --query "Vpcs[0].VpcId" --output text)
aws ec2 detach-internet-gateway --internet-gateway-id $IGW_ID --vpc-id $VPC_ID
aws ec2 delete-internet-gateway --internet-gateway-id $IGW_ID

# 4. Delete Subnet
SUBNET_ID=$(aws ec2 describe-subnets \
    --filters "Name=tag:Name,Values=lakehouse-public-subnet" \
    --query "Subnets[0].SubnetId" --output text)
aws ec2 delete-subnet --subnet-id $SUBNET_ID

# 5. Delete VPC
aws ec2 delete-vpc --vpc-id $VPC_ID
```

---

### Step 8: Delete IAM Roles

```bash
# Detach policies from Glue role
aws iam detach-role-policy \
    --role-name AWSGlueServiceRole-lakehouse \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole
aws iam detach-role-policy \
    --role-name AWSGlueServiceRole-lakehouse \
    --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess

# Delete Glue role
aws iam delete-role --role-name AWSGlueServiceRole-lakehouse

# Detach policies from EC2 role
aws iam detach-role-policy \
    --role-name lakehouse-ec2-role \
    --policy-arn arn:aws:iam::aws:policy/AmazonAthenaFullAccess
aws iam detach-role-policy \
    --role-name lakehouse-ec2-role \
    --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess

# Delete EC2 role
aws iam delete-role --role-name lakehouse-ec2-role
```

---

### Step 9: Delete SNS Topic (Alerts)

```bash
# Find SNS topic ARN
SNS_ARN=$(aws sns list-topics --query "Topics[?contains(TopicArn,'lakehouse')].TopicArn" --output text)

# Delete it
aws sns delete-topic --topic-arn $SNS_ARN
```

---

### Step 10: Delete Firehose Stream (if created)

```bash
aws firehose delete-delivery-stream --delivery-stream-name lakehouse-event-stream
```

---

## Final Verification

Run this to check for any remaining billable resources:

```bash
echo "=== Checking for remaining resources ==="

echo "--- EC2 Instances ---"
aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" \
    --query "Reservations[*].Instances[*].{ID:InstanceId,Type:InstanceType,State:State.Name}" \
    --output table

echo "--- Elastic IPs ---"
aws ec2 describe-addresses --query "Addresses[*].{IP:PublicIp,AssocId:AssociationId}" \
    --output table

echo "--- S3 Buckets ---"
aws s3 ls | grep lakehouse

echo "--- Glue Jobs ---"
aws glue list-jobs --query "JobNames" --output text | tr '\t' '\n' | grep lakehouse

echo "--- CloudWatch Alarms ---"
aws cloudwatch describe-alarms --query "MetricAlarms[?contains(AlarmName,'lakehouse')].AlarmName" \
    --output text
```

Expected output: All sections should be empty (no remaining resources).

---

## Clean-up Summary Checklist

- [ ] EC2 instance terminated
- [ ] Elastic IP released
- [ ] 3 Glue ETL jobs deleted
- [ ] 7 Glue Catalog tables deleted
- [ ] Glue database deleted
- [ ] S3 bucket emptied and deleted
- [ ] CloudWatch alarms deleted
- [ ] CloudWatch dashboard deleted
- [ ] CloudWatch log groups deleted
- [ ] VPC, Subnet, IGW, Route Table, Security Group deleted
- [ ] IAM roles (Glue + EC2) deleted
- [ ] SNS topic deleted
- [ ] Firehose stream deleted (if created)

✅ **Workshop complete!** All resources cleaned up. No further charges will be incurred.
