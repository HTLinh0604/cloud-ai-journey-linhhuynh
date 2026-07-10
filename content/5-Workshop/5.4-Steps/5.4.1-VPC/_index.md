---
title: "Step 1: VPC & Networking"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 5.4.1 </b> "
---

# Step 1: VPC & Networking Setup

In this step, you will create the network foundation for the workshop: a VPC with a public subnet, Internet Gateway, Route Table, and Security Group to host the EC2 Streamlit dashboard.

**Estimated time:** 15–20 minutes

---

## 1.1 Create a VPC

**AWS Console → VPC → Your VPCs → Create VPC**

| Field | Value |
|-------|-------|
| Name tag | `lakehouse-vpc` |
| IPv4 CIDR block | `10.0.0.0/16` |
| IPv6 CIDR block | No IPv6 CIDR block |
| Tenancy | Default |

Click **Create VPC**.

> 📌 **[INSERT SCREENSHOT: VPC created successfully]**
> `![VPC](/result/VPC/Your VPCs..jpg)`

---

## 1.2 Create a Public Subnet

**VPC Console → Subnets → Create Subnet**

| Field | Value |
|-------|-------|
| VPC | Select `lakehouse-vpc` |
| Subnet name | `lakehouse-public-subnet` |
| Availability Zone | `us-east-1a` |
| IPv4 CIDR block | `10.0.1.0/24` |

Click **Create Subnet**.

After creating, select the subnet → **Actions → Edit subnet settings**:
- ✅ Enable **Auto-assign public IPv4 address**

> 📌 **[INSERT SCREENSHOT: Subnet created]**
> `![Subnets](/result/VPC/Subnets.jpg)`

---

## 1.3 Create and Attach an Internet Gateway

**VPC Console → Internet Gateways → Create Internet Gateway**

| Field | Value |
|-------|-------|
| Name tag | `lakehouse-igw` |

Click **Create Internet Gateway**.

Then **Actions → Attach to VPC** → select `lakehouse-vpc` → **Attach internet gateway**.

> 📌 **[INSERT SCREENSHOT: Internet Gateway attached]**
> `![Internet Gateway](/result/VPC/Internet Gateway.jpg)`

---

## 1.4 Configure Route Table

**VPC Console → Route Tables**

Select the Route Table associated with `lakehouse-vpc` (or create a new one named `lakehouse-rt`).

**Routes tab → Edit routes → Add route:**

| Destination | Target |
|-------------|--------|
| `0.0.0.0/0` | `lakehouse-igw` (Internet Gateway) |

Click **Save changes**.

**Subnet associations tab → Edit subnet associations:**
- Select `lakehouse-public-subnet`

Click **Save associations**.

> 📌 **[INSERT SCREENSHOT: Route Table with 0.0.0.0/0 → IGW route]**
> `![Route Tables](/result/VPC/Route Tables.jpg)`

---

## 1.5 Create a Security Group for EC2

**VPC Console → Security Groups → Create Security Group**

| Field | Value |
|-------|-------|
| Security group name | `lakehouse-ec2-sg` |
| Description | `Allow SSH and Streamlit access` |
| VPC | `lakehouse-vpc` |

**Inbound rules - Add rules:**

| Type | Protocol | Port | Source | Description |
|------|----------|------|--------|-------------|
| SSH | TCP | 22 | `My IP` | SSH management access |
| Custom TCP | TCP | 8501 | `0.0.0.0/0` | Streamlit dashboard |

**Outbound rules:** Leave default (all traffic allowed).

Click **Create security group**.

> ⚠️ **Security note:** In production, restrict port 8501 to your company's IP range rather than `0.0.0.0/0`. For this workshop, allowing all IPs is acceptable for a temporary test environment.

> 📌 **[INSERT SCREENSHOT: Security Group inbound rules]**
> `![Security Group](/result/VPC/Security Group.jpg)`

---

## 1.6 Validation

Verify your networking setup:

```bash
# Verify VPC exists
aws ec2 describe-vpcs --filters "Name=tag:Name,Values=lakehouse-vpc" \
    --query "Vpcs[0].{VpcId:VpcId,CIDR:CidrBlock,State:State}"

# Verify subnet
aws ec2 describe-subnets --filters "Name=tag:Name,Values=lakehouse-public-subnet" \
    --query "Subnets[0].{SubnetId:SubnetId,CIDR:CidrBlock,AZ:AvailabilityZone}"

# Verify Internet Gateway
aws ec2 describe-internet-gateways --filters "Name=tag:Name,Values=lakehouse-igw" \
    --query "InternetGateways[0].{IGWId:InternetGatewayId,Attachments:Attachments}"
```

Expected outputs show the created resources in `available` state.

✅ **Step 1 complete** - Proceed to [Step 2: S3 Buckets & Data Upload](../5.4.2-S3/)
