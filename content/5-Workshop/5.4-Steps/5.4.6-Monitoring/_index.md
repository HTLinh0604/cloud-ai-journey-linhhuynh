---
title: "Step 6: Monitoring"
date: 2024-01-01
weight: 6
chapter: false
pre: " <b> 5.4.6 </b> "
---

# Step 6: Monitoring with CloudWatch

In this step, you will set up monitoring and alerting for the entire data pipeline using Amazon CloudWatch - covering Glue ETL job health, Athena query metrics, Lambda invocations, and EC2 instance health.

**Estimated time:** 20–25 minutes

---

## 6.1 View Glue ETL Job Logs

**AWS Console → AWS Glue → ETL Jobs → [job name] → Runs tab**

Each job run generates logs in CloudWatch Logs:

**CloudWatch Console → Log groups → `/aws-glue/jobs/output`**

Or view directly:
```bash
# Get the log stream name for a specific run
aws glue get-job-runs --job-name silver-to-gold-job \
    --query "JobRuns[0].{Status:JobRunState,LogGroup:LogGroupName,Duration:ExecutionTime}"

# Tail job logs
aws logs tail /aws-glue/jobs/output --follow
```

**Key log messages to look for:**

```
Reading Silver: s3://customer-behavior-lakehouse1/silver/events/
Writing Gold: s3://customer-behavior-lakehouse1/gold/event_summary/
Registered Glue Catalog table: event_summary
Silver to Gold job completed and Glue Catalog tables registered.
```

---

## 6.2 Set Up CloudWatch Alarms for Glue Jobs

**AWS Console → CloudWatch → Alarms → Create alarm**

**Alarm 1: Glue Job Failure Alert**

| Field | Value |
|-------|-------|
| Metric | Glue → `glue.driver.aggregate.numFailedTasks` |
| Statistic | Sum |
| Period | 5 minutes |
| Threshold | `> 0` |
| Alarm name | `GlueJobFailure-Alert` |
| Notification | Create SNS topic → add your email |

This alarm fires whenever any task in a Glue job fails, sending you an email notification immediately.

**CLI alternative:**
```bash
# Create SNS topic
aws sns create-topic --name lakehouse-alerts
# (Subscribe your email to the topic via SNS console)

# Create Glue failure alarm
aws cloudwatch put-metric-alarm \
    --alarm-name "GlueJobFailure-Alert" \
    --alarm-description "Alert when Glue ETL job has failed tasks" \
    --metric-name "glue.driver.aggregate.numFailedTasks" \
    --namespace "Glue" \
    --statistic Sum \
    --period 300 \
    --threshold 0 \
    --comparison-operator GreaterThanThreshold \
    --evaluation-periods 1 \
    --alarm-actions arn:aws:sns:us-east-1:<account-id>:lakehouse-alerts
```

---

## 6.3 Set Up CloudWatch Alarms for Athena

**Alarm 2: Athena Data Scan Cost Alert**

Monitors the total data scanned per day - alerts if you're approaching cost limits.

```bash
aws cloudwatch put-metric-alarm \
    --alarm-name "Athena-DataScan-Alert" \
    --alarm-description "Alert when Athena scans more than 5 GB in a day" \
    --metric-name "DataScannedInBytes" \
    --namespace "AWS/Athena" \
    --dimensions Name=WorkGroup,Value=lakehouse-wg \
    --statistic Sum \
    --period 86400 \
    --threshold 5368709120 \
    --comparison-operator GreaterThanThreshold \
    --evaluation-periods 1 \
    --alarm-actions arn:aws:sns:us-east-1:<account-id>:lakehouse-alerts
```

---

## 6.4 Monitor EC2 Instance Health

**CloudWatch Console → All metrics → EC2 → Per-Instance Metrics**

Select `lakehouse-dashboard` instance and view:
- **CPUUtilization** - should be low (~5–20%) at idle
- **NetworkIn/NetworkOut** - traffic from users accessing the dashboard

**Alarm 3: EC2 CPU High Alert**

```bash
aws cloudwatch put-metric-alarm \
    --alarm-name "EC2-CPU-High-Alert" \
    --alarm-description "EC2 CPU above 80% for 5 minutes" \
    --metric-name "CPUUtilization" \
    --namespace "AWS/EC2" \
    --dimensions Name=InstanceId,Value=<your-ec2-instance-id> \
    --statistic Average \
    --period 300 \
    --threshold 80 \
    --comparison-operator GreaterThanThreshold \
    --evaluation-periods 1 \
    --alarm-actions arn:aws:sns:us-east-1:<account-id>:lakehouse-alerts
```

---

## 6.5 Create a CloudWatch Dashboard

Create a unified dashboard to view all pipeline health metrics in one place.

**CloudWatch Console → Dashboards → Create dashboard**

| Field | Value |
|-------|-------|
| Dashboard name | `lakehouse-pipeline-health` |

Add the following widgets:

| Widget | Metric | Chart Type |
|--------|--------|-----------|
| Glue Job Runs | `Glue / glue.driver.aggregate.numCompletedTasks` | Line |
| Glue Failed Tasks | `Glue / glue.driver.aggregate.numFailedTasks` | Line |
| Athena Data Scanned | `AWS/Athena / DataScannedInBytes` | Bar |
| EC2 CPU | `AWS/EC2 / CPUUtilization` | Line |
| S3 Bucket Size | `AWS/S3 / BucketSizeBytes` per tier | Line |

**CLI to create dashboard:**
```bash
aws cloudwatch put-dashboard \
    --dashboard-name "lakehouse-pipeline-health" \
    --dashboard-body '{
        "widgets": [
            {
                "type": "metric",
                "properties": {
                    "title": "EC2 CPU Utilization",
                    "metrics": [["AWS/EC2","CPUUtilization","InstanceId","<instance-id>"]],
                    "period": 300,
                    "stat": "Average"
                }
            },
            {
                "type": "metric",
                "properties": {
                    "title": "Athena Data Scanned (Bytes)",
                    "metrics": [["AWS/Athena","DataScannedInBytes","WorkGroup","lakehouse-wg"]],
                    "period": 86400,
                    "stat": "Sum"
                }
            }
        ]
    }'
```

---

## 6.6 View Lambda Logs (Ingestion Path)

If you used Lambda for Firehose transformation or batch DB extraction:

**CloudWatch Console → Log groups → `/aws/lambda/<function-name>`**

```bash
# List log streams for Lambda
aws logs describe-log-streams \
    --log-group-name /aws/lambda/firehose-transform \
    --query "logStreams[-1].logStreamName" \
    --output text

# Get last 20 log events
aws logs get-log-events \
    --log-group-name /aws/lambda/firehose-transform \
    --log-stream-name <log-stream-name> \
    --limit 20 \
    --query "events[*].message" \
    --output text
```

---

## 6.7 Summary: Alarms Configured

| Alarm Name | Metric | Threshold | Action |
|------------|--------|-----------|--------|
| `GlueJobFailure-Alert` | `numFailedTasks` | > 0 | SNS email |
| `Athena-DataScan-Alert` | `DataScannedInBytes` | > 5 GB/day | SNS email |
| `EC2-CPU-High-Alert` | `CPUUtilization` | > 80% for 5 min | SNS email |

---

## 6.8 Test Alerting

Trigger a test alarm to verify SNS notifications are working:

```bash
# Force an alarm state change to ALARM (test only)
aws cloudwatch set-alarm-state \
    --alarm-name "GlueJobFailure-Alert" \
    --state-value ALARM \
    --state-reason "Test alarm trigger"

# Check your email for the SNS notification
# Then reset back to OK
aws cloudwatch set-alarm-state \
    --alarm-name "GlueJobFailure-Alert" \
    --state-value OK \
    --state-reason "Test complete"
```

✅ **Step 6 complete** - Your pipeline is fully monitored. Proceed to [Clean-up](../../5.5-Cleanup/) when finished.
