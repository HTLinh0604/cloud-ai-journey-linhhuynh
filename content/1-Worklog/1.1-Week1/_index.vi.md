---
title: "Worklog Tuần 1"
date: 2026-04-27
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---

> **Tuần 1 — Khởi động hành trình Cloud AI:** Làm quen với hệ sinh thái AWS, hoàn thành 5 nhiệm vụ tích lũy credit và thiết lập nền tảng giám sát chi phí.

---

### Mục tiêu tuần 1

* Tạo và thiết lập tài khoản AWS, nhận **$200 credit** thông qua các nhiệm vụ thực hành.
* Làm quen với hạ tầng toàn cầu của AWS và các dịch vụ cốt lõi: EC2, S3, IAM, VPC, RDS, Lambda, Bedrock.
* Thiết lập hệ thống giám sát và kiểm soát chi phí (AWS Budgets, CloudWatch, Cost Explorer).
* Nắm vững các khái niệm nền tảng: Cloud Computing, bảo mật AWS, quản lý danh tính (IAM), mạng (VPC).

---

### Lịch công việc tuần 1

| Thứ | Công việc | Ngày | Nguồn tài liệu |
| --- | --------- | ---- | -------------- |
| **2** | - Tạo tài khoản AWS & nhận $100 credit khởi động <br> - Hoàn thành **5 Tasks** để tích lũy thêm $100 credit: <br>&emsp; + Task 1: Launch EC2 Instance (+$20) <br>&emsp; + Task 2: Amazon Bedrock Playground (+$20) <br>&emsp; + Task 3: Set up AWS Budgets (+$20) <br>&emsp; + Task 4: Create Lambda Web App (+$20) <br>&emsp; + Task 5: Create RDS Database (+$20) <br> - Nội dung đã học: <br>&emsp; + Creating Your First AWS Account <br>&emsp; + Managing Costs with AWS Budgets <br>&emsp; + Getting Help with AWS Support <br>&emsp; + Access Management with AWS IAM <br>&emsp; + Networking Essentials with Amazon VPC | 20/04/2026 | [cloudjourney.awsstudygroup.com](https://cloudjourney.awsstudygroup.com/) |
| **4** | - Thiết lập hệ thống **Basic Monitoring** toàn diện <br>&emsp; + Cấu hình AWS Budgets (3 mức ngưỡng cảnh báo) <br>&emsp; + Tạo CloudWatch Alarms (Email / SMS / Slack) <br>&emsp; + Kích hoạt Cost Explorer & báo cáo hàng ngày <br> - Nghiên cứu **Advanced Analytics** <br>&emsp; + Custom CloudWatch Metrics <br>&emsp; + Resource Tagging Strategy <br> - Xây dựng **Emergency Cost Control Protocol** <br> - Học lý thuyết nền tảng AWS <br> - Nội dung đã học: <br>&emsp; + Compute Essentials with Amazon EC2 <br>&emsp; + Instance Profiling with IAM Roles for EC2 <br>&emsp; + Cloud Development with AWS Cloud9 <br>&emsp; + Static Website Hosting with Amazon S3 <br>&emsp; + Database Essentials with Amazon RDS | 22/04/2026 | [cloudjourney.awsstudygroup.com](https://cloudjourney.awsstudygroup.com/) |

---

### Chi tiết công việc

#### Ngày 1 — Thứ 2, 20/04/2026: Kích hoạt tài khoản & Hoàn thành 5 Tasks

##### Tạo tài khoản AWS — Nhận $100 Credit

Bước đầu tiên trong hành trình là đăng ký tài khoản AWS. Sau khi tạo thành công và xác minh danh tính, tài khoản tự động nhận được **$100 credit khởi động** từ AWS.

---

##### Task 1: Launch EC2 Instance +$20 Credit

**Mục tiêu:** Tạo và quản lý máy ảo (Virtual Machine) trên AWS Cloud.

**EC2 (Elastic Compute Cloud)** là dịch vụ điện toán cốt lõi của AWS, cho phép khởi tạo máy chủ ảo với nhiều cấu hình phần cứng và hệ điều hành linh hoạt.

Các bước thực hiện:
1. Truy cập **AWS Console** → Widget "Explore AWS" → Chọn task **Launch an instance using EC2**.
2. Nhấn **Start activity** để bắt đầu.
3. Đặt tên Instance: `Test Instance` → Chọn AMI phù hợp.
4. Giữ nguyên cấu hình phần cứng mặc định.
5. Tạo Key Pair mới: Tên `first-kp` | Loại **RSA** | Định dạng **.pem**
6. Tạo Security Group với các quy tắc mặc định.
7. Review cấu hình → **Launch Instance**.
8. **Clean up:** Terminate instance sau khi hoàn thành để tránh phát sinh chi phí.

> **Bài học:** Luôn dọn dẹp tài nguyên ngay sau khi thực hành để tối ưu chi phí.

---

##### Task 2: Amazon Bedrock Playground +$20 Credit

**Mục tiêu:** Trải nghiệm AI/ML với các Foundation Models trên AWS.

**Amazon Bedrock** là dịch vụ fully-managed cung cấp quyền truy cập vào các foundation model hàng đầu (Claude, Llama, Titan,...) thông qua một API thống nhất.

Các bước thực hiện:
1. Truy cập **Bedrock Console** → Chọn task **Use a foundation model in Amazon Bedrock**.
2. Chọn model: **Claude 3 Haiku** (cân bằng tốt giữa hiệu suất và chi phí).
3. Điền thông tin use case và submit, đợi phê duyệt. Nếu gặp lỗi authorization, tạo **Support Case** với AWS (Category: Bedrock Allowlisting).
4. Sau khi được phê duyệt: Viết prompt test → **Run** → Review kết quả → **Finish**.

> **Bài học:** Một số dịch vụ AI của AWS yêu cầu phê duyệt use case trước khi sử dụng — đây là biện pháp kiểm soát sử dụng có trách nhiệm (Responsible AI).

---

##### Task 3: Set up AWS Budgets +$20 Credit

**Mục tiêu:** Thiết lập hệ thống monitoring và cảnh báo chi phí.

**AWS Budgets** cho phép đặt ngưỡng chi phí và nhận thông báo tự động khi sắp vượt mức cho phép.

Các bước thực hiện:
1. Truy cập **Budgets Console** → Chọn task **Set up a cost budget using AWS Budgets**.
2. Nhấn **Start activity** → Cấu hình thông số budget.
3. Nhập địa chỉ email nhận thông báo → **Create budget**.
4. Budget được tạo thành công với thông báo email tự động.

---

##### Task 4: Create Lambda Web App +$20 Credit

**Mục tiêu:** Xây dựng serverless web application trên AWS.

**AWS Lambda** là dịch vụ compute serverless — chạy code mà không cần quản lý server, chỉ trả tiền cho thời gian thực thi thực tế.

Các bước thực hiện:
1. Truy cập **Lambda Console** → Chọn task **Create a web app using AWS Lambda**.
2. Nhấn **Start activity** → Chọn **Use a blueprint** → **Getting started with Lambda HTTP**.
3. Đặt tên function: `http-function-url-tutorial`.
4. Tick **Acknowledgment** → **Create function** thành công.
5. **Clean up:** Delete function sau khi hoàn thành.

> **Bài học:** Serverless architecture loại bỏ hoàn toàn nhu cầu provisioning server — phù hợp cho các workload có traffic không đều.

---

##### Task 5: Create RDS Database +$20 Credit

**Mục tiêu:** Thiết lập managed relational database trên AWS.

**Amazon RDS (Relational Database Service)** quản lý toàn bộ vòng đời của database: backup, patching, scaling.

Các bước thực hiện:
1. Truy cập **RDS Console** → Chọn task **Create an Amazon RDS Database**.
2. Chọn **Easy create** → Engine: **Aurora (PostgreSQL Compatible)**.
3. **Create database** → Đợi trạng thái chuyển sang **Available**.
4. **Clean up (theo thứ tự):** Xóa instance `database-1-instance-1` trước, sau đó xóa cluster `database-1`.

> **Lưu ý:** Phải xóa instance trước rồi mới xóa cluster, ngược lại sẽ gặp lỗi dependency.

---

#### Ngày 2 — Thứ 4, 22/04/2026: Monitoring, Analytics & Học lý thuyết nền tảng

##### Basic Monitoring — Thiết lập giám sát chi phí

**1. AWS Budgets (3 mức cảnh báo)**

| Budget | Ngưỡng | Alert |
|--------|--------|-------|
| Budget 1 | $50/tháng | Cảnh báo tại 80% ($40) |
| Budget 2 | $25/tháng | Cảnh báo tại 50% ($12.5) |
| Budget 3 | $10/ngày | Cảnh báo tại 100% ($10) |

**2. Billing Alerts qua CloudWatch Alarms**

| Ngưỡng | Kênh thông báo |
|--------|---------------|
| $25 | Email warning |
| $50 | Email + SMS |
| $75 | Email + SMS + Slack |

**3. Cost Explorer**
- Kích hoạt **daily cost reports** để theo dõi chi phí hàng ngày.
- Thiết lập **service-level breakdown** — phân tích chi phí theo từng dịch vụ.
- Monitor **top 5 cost drivers** để nhanh chóng xác định nguồn chi phí cao nhất.

---

##### Advanced Analytics

**Custom CloudWatch Metrics:**
Tạo các metric tùy chỉnh để theo dõi các chỉ số business-specific vượt ra ngoài các metric mặc định của AWS.

**Resource Tagging Strategy:**
Áp dụng tagging nhất quán cho mọi resource AWS giúp phân bổ chi phí chính xác theo team, project và môi trường (dev/staging/prod).

---

##### Emergency Cost Control Protocol

**Immediate Resource Audit:**
Kiểm tra và liệt kê toàn bộ tài nguyên đang chạy khi phát hiện chi phí bất thường.

**Emergency Shutdown Protocol:**
Quy trình tắt khẩn cấp các tài nguyên không thiết yếu để ngăn chặn chi phí leo thang — đặc biệt quan trọng trong môi trường học tập.

---

##### Kiến thức lý thuyết nền tảng

**Tổng quan Cloud Computing:**
- Hiểu rõ lợi ích của điện toán đám mây: elasticity, pay-as-you-go, global reach.
- Phân biệt các mô hình dịch vụ: **IaaS, PaaS, SaaS**.
- So sánh mô hình triển khai: Public Cloud, Private Cloud, Hybrid Cloud.

**Hạ tầng toàn cầu AWS:**
- **Regions:** Các khu vực địa lý độc lập (~30+ regions toàn cầu).
- **Availability Zones (AZs):** Các data center riêng biệt trong một Region, đảm bảo High Availability.
- **Edge Locations:** Điểm phân phối nội dung (CDN) cho CloudFront, giảm latency.

**Bảo mật AWS:**
- **Root Account:** Tài khoản cấp cao nhất — chỉ dùng cho cấu hình ban đầu, bảo vệ bằng MFA.
- **IAM Users/Groups/Policies:** Phân quyền chi tiết theo nguyên tắc **Least Privilege**.
- **MFA (Multi-Factor Authentication):** Bắt buộc cho Root và IAM users có quyền cao.

**Quản lý chi phí:**
- **AWS Free Tier:** 12 tháng miễn phí cho các dịch vụ đủ điều kiện.
- **AWS Budgets:** Cảnh báo chi phí proactive.
- **Cost Explorer:** Phân tích chi phí theo thời gian và dịch vụ.

**Dịch vụ cốt lõi:**
- **Amazon S3:** Object storage với độ bền 99.999999999% (11 nines).
- **Amazon EC2:** Compute linh hoạt với đa dạng instance types.

---

##### Nội dung đã học được

| Ngày | Chủ đề |
|------|--------|
| 20/4 | Creating Your First AWS Account |
| 20/4 | Managing Costs with AWS Budgets |
| 20/4 | Getting Help with AWS Support |
| 20/4 | Access Management with AWS Identity and Access Management (IAM) |
| 20/4 | Networking Essentials with Amazon Virtual Private Cloud (VPC) |
| 22/4 | Compute Essentials with Amazon Elastic Compute Cloud (EC2) |
| 22/4 | Instance Profiling with IAM Roles for EC2 |
| 22/4 | Cloud Development with AWS Cloud9 |
| 22/4 | Static Website Hosting with Amazon S3 |
| 22/4 | Database Essentials with Amazon Relational Database Service (RDS) |

---

### Kết quả đạt được tuần 1

* **Tài khoản AWS** được tạo và cấu hình thành công với đầy đủ bảo mật (MFA, IAM).
* **$200 AWS Credit** tích lũy thành công: $100 khởi động từ AWS + $100 từ 5 tasks thực hành.
* **5 dịch vụ AWS cốt lõi** được thực hành trực tiếp: EC2, Bedrock, Budgets, Lambda, RDS.
* **Hệ thống monitoring chi phí** 3 lớp được thiết lập: Budgets → CloudWatch Alarms → Cost Explorer.
* **Kiến thức lý thuyết nền tảng** vững chắc: Cloud Computing, AWS Global Infrastructure, IAM, Networking.
* Hiểu và áp dụng nguyên tắc **"Clean up after practice"** — luôn dọn dẹp tài nguyên sau thực hành.

---

*Nguồn tài liệu chính: [First Cloud Journey — AWS Study Group](https://cloudjourney.awsstudygroup.com/)*
