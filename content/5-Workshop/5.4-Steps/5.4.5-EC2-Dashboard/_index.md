---
title: "Step 5: EC2 & Dashboard"
date: 2024-01-01
weight: 5
chapter: false
pre: " <b> 5.4.5 </b> "
---

# Step 5: Deploy Streamlit Dashboard on EC2

In this step, you will launch an EC2 instance inside the VPC created in Step 1, assign it an IAM role with Athena access, install the required Python packages, deploy the `app_beautiful.py` Streamlit application, and access the live analytics dashboard.

**Estimated time:** 25–35 minutes

---

## 5.1 Create an IAM Role for EC2

The EC2 instance needs permissions to query Athena and read S3 results.

**AWS Console → IAM → Roles → Create role**

| Field | Value |
|-------|-------|
| Trusted entity type | AWS service |
| Service | EC2 |

**Add permissions:**
- `AmazonAthenaFullAccess`
- `AmazonS3ReadOnlyAccess` (for reading Gold and athena-results)

**Role name:** `lakehouse-ec2-role`

> ⚠️ **Least-privilege note:** In production, replace `AmazonS3ReadOnlyAccess` with a custom policy granting `s3:GetObject` only on `s3://customer-behavior-lakehouse1/gold/*` and `s3://customer-behavior-lakehouse1/athena-results/*`. The EC2 instance should never need to write to S3 or access Bronze/Silver.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["athena:StartQueryExecution", "athena:GetQueryResults", "athena:GetQueryExecution"],
      "Resource": "arn:aws:athena:us-east-1:*:workgroup/lakehouse-wg"
    },
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:ListBucket"],
      "Resource": [
        "arn:aws:s3:::customer-behavior-lakehouse1/gold/*",
        "arn:aws:s3:::customer-behavior-lakehouse1/athena-results/*",
        "arn:aws:s3:::customer-behavior-lakehouse1"
      ]
    },
    {
      "Effect": "Allow",
      "Action": ["glue:GetTable", "glue:GetTables", "glue:GetDatabase", "glue:GetPartitions"],
      "Resource": "*"
    }
  ]
}
```

---

## 5.2 Launch EC2 Instance

**AWS Console → EC2 → Instances → Launch instances**

| Field | Value |
|-------|-------|
| Name | `lakehouse-dashboard` |
| AMI | Amazon Linux 2023 AMI (free tier eligible) |
| Instance type | `t3.micro` (Free Tier eligible) |
| Key pair | Create new: `lakehouse-key` → Download `.pem` file |
| VPC | `lakehouse-vpc` |
| Subnet | `lakehouse-public-subnet` |
| Auto-assign public IP | Enable |
| Security group | Select existing: `lakehouse-ec2-sg` |
| IAM instance profile | `lakehouse-ec2-role` |
| Storage | 8 GiB gp3 (default EBS) |

Click **Launch instance**.

> 📌 **[INSERT SCREENSHOT: EC2 Instance running]**
> `![EC2 Instance](/result/EC2/EC2 Instance.jpg)`

> 📌 **[INSERT SCREENSHOT: EC2 Security Group rules]**
> `![EC2 Security Group](/result/EC2/Security Group.jpg)`

---

## 5.3 Assign an Elastic IP (Optional but Recommended)

An Elastic IP ensures the dashboard URL doesn't change if the EC2 instance is stopped and restarted.

**AWS Console → EC2 → Elastic IPs → Allocate Elastic IP address**

- Click **Allocate** (default settings)

Then **Actions → Associate Elastic IP address**:
- Instance: select `lakehouse-dashboard`
- Click **Associate**

Note the Elastic IP address - this will be your dashboard URL: `http://<elastic-ip>:8501`

---

## 5.4 Connect to EC2 and Set Up Environment

SSH into the instance:

```bash
# On your local machine
chmod 400 lakehouse-key.pem
ssh -i lakehouse-key.pem ec2-user@<elastic-ip-or-public-ip>
```

Once connected, install Python dependencies:

```bash
# Update system
sudo dnf update -y

# Install Python pip
sudo dnf install python3-pip -y

# Install required packages
pip3 install boto3 pandas streamlit plotly awswrangler pyathena

# Verify installation
python3 -c "import streamlit; print('Streamlit version:', streamlit.__version__)"
python3 -c "import awswrangler; print('AWS Wrangler version:', awswrangler.__version__)"
```

---

## 5.5 Deploy the Streamlit Application

Transfer the `app_beautiful.py` file to the EC2 instance:

```bash
# From your local machine (in a second terminal)
scp -i lakehouse-key.pem app_beautiful.py ec2-user@<elastic-ip>:~/app_beautiful.py
```

Or copy-paste the code directly in the EC2 SSH session:

```bash
# On EC2: create the file
cat > ~/app_beautiful.py << 'EOF'
[paste contents of app_beautiful.py here]
EOF
```

**Verify the AWS configuration inside the app:**

The app file contains these settings - confirm they match your setup:
```python
DATABASE = "customer_behavior_catalog_db"         # ← Your Glue database
ATHENA_OUTPUT = "s3://customer-behavior-lakehouse1/athena-results/"   # ← Your results bucket
REGION = "us-east-1"                              # ← Your region
```

---

## 5.6 Run the Dashboard

```bash
# Start Streamlit in the background (so it continues after you close SSH)
nohup streamlit run app_beautiful.py --server.port 8501 --server.address 0.0.0.0 > streamlit.log 2>&1 &

# Check it started
sleep 3
cat streamlit.log
# Expected: "You can now view your Streamlit app in your browser"
# Expected: Local URL: http://0.0.0.0:8501

# Verify port is listening
ss -tlnp | grep 8501
```

**Access the dashboard:**

Open your browser and navigate to:
```
http://<elastic-ip>:8501
```

> 📌 **[INSERT SCREENSHOT: Streamlit Dashboard - Revenue Trend chart]**
> `![Revenue Trend](/result/DashBoard/Revenue Trend.png)`

> 📌 **[INSERT SCREENSHOT: Streamlit Dashboard - Event Distribution]**
> `![Event Distribution](/result/DashBoard/Event Distribution.png)`

> 📌 **[INSERT SCREENSHOT: Streamlit Dashboard - Revenue by Device]**
> `![Revenue by Device](/result/DashBoard/Revenue by Device.png)`

> 📌 **[INSERT SCREENSHOT: Streamlit Dashboard - Revenue by Payment Method]**
> `![Revenue by Payment](/result/DashBoard/Revenue by Payment Method.png)`

> 📌 **[INSERT SCREENSHOT: Streamlit Dashboard - Top 10 Countries by Revenue]**
> `![Top Countries](/result/DashBoard/Top 10 Countries by Revenue.png)`

> 📌 **[INSERT SCREENSHOT: Streamlit Dashboard - Revenue by Traffic Source]**
> `![Traffic Source](/result/DashBoard/Revenue by Traffic Source.png)`

> 📌 **[INSERT SCREENSHOT: Streamlit Dashboard - Top Performers table]**
> `![Top Performers](/result/DashBoard/Top Performers.jpg)`

> 📌 **[INSERT SCREENSHOT: Streamlit Dashboard - View Daily Revenue Data]**
> `![Daily Revenue Data](/result/DashBoard/View Daily Revenue Data.jpg)`

---

## 5.7 Validate the Dashboard

Verify each section of the dashboard works correctly:

| Dashboard Section | Expected Content | Validation |
|------------------|-----------------|------------|
| **KPI Cards** | 5 metrics: Orders, Customers, Revenue, Avg Order, Events | Numbers > 0 |
| **Executive Summary** | Business highlights and quick facts | Top country, device, payment method shown |
| **Revenue Trend** | Area chart showing daily revenue over time | Chart renders with x-axis dates, y-axis in $ |
| **Event Distribution** | Bar chart by event type | At least 3–5 event types shown |
| **Top 10 Countries** | Horizontal bar chart | Countries sorted by revenue |
| **Revenue by Device** | Donut chart | mobile, desktop, tablet shown |
| **Revenue by Payment** | Bar chart | credit_card, paypal, bank_transfer |
| **Revenue by Traffic Source** | Bar chart | organic, social, email, paid_ads |
| **Top Performers** | 3-column table | Top 5 for countries, devices, sources |
| **Daily Revenue Data** | Expandable data table | Full date-sorted table loads |
| **Dashboard Summary** | Key findings text | All KPIs correctly summarized |

**Test data refresh (cache):**
The app uses `@st.cache_data(ttl=600)` - data is cached for 10 minutes. To force a refresh, add `?cache_buster=1` to the URL or click the **⋮** menu → **Clear cache**.

---

## 5.8 Keep Dashboard Running (Persistent)

To ensure the dashboard keeps running after you close the SSH session:

```bash
# Check running processes
ps aux | grep streamlit

# View logs
tail -f ~/streamlit.log

# Stop the dashboard (when needed)
pkill -f streamlit
```

For a more robust setup, create a systemd service:

```bash
sudo tee /etc/systemd/system/streamlit.service << EOF
[Unit]
Description=Streamlit Dashboard
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/home/ec2-user
ExecStart=/usr/local/bin/streamlit run /home/ec2-user/app_beautiful.py --server.port 8501 --server.address 0.0.0.0
Restart=always

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable streamlit
sudo systemctl start streamlit
sudo systemctl status streamlit
```

✅ **Step 5 complete** - Proceed to [Step 6: Monitoring with CloudWatch](../5.4.6-Monitoring/)
