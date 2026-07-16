---
title: "Tuần 2"
date: 2026-04-27
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

Mục tiêu tuần:
- Cấu hình các thiết lập nâng cao và chính sách vòng đời tối ưu chi phí của S3.
- Hiểu các loại EBS volume, cách gắn volume thủ công và tạo snapshot để dự phòng.
- Thiết lập quản lý vòng đời snapshot tự động cho EBS.
- Triển khai và cấu hình các instance cơ sở dữ liệu Amazon RDS trong subnet tùy chỉnh.

Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày |
|---|---|---|
| Thứ Hai | Cấu hình lưu trữ trang web tĩnh và các chính sách chuyển đổi dữ liệu trong Amazon S3. | 27/4 |
| Thứ Ba | Tạo và gắn các volume EBS vào instance và tiến hành tạo snapshot thủ công. | 28/4 |
| Thứ Tư | Triển khai các quy tắc vòng đời snapshot tự động bằng EBS Data Lifecycle Manager. | 29/4 |
| Thứ Năm | Khởi tạo các instance Amazon RDS PostgreSQL và quản lý các DB subnet group. | 30/4 |
| Thứ Sáu | Cấu hình triển khai cơ sở dữ liệu Multi-AZ và áp dụng các quy tắc bảo mật security group cho database. | 1/5 |

Kết quả đạt được trong tuần là gì:
- Kích hoạt thành công tối ưu hóa chi phí tự động bằng cách chuyển đổi các đối tượng S3 cũ sang các tầng lưu trữ lạnh hơn.
- Thực hiện thành thạo các thao tác trên volume và tạo điểm khôi phục cho các instance EC2.
- Tự động hóa quy trình sao lưu hệ thống bằng EBS Data Lifecycle Manager.
- Triển khai thành công các mô hình truy cập cơ sở dữ liệu an toàn bằng cách cô lập security group trong các subnet VPC tùy chỉnh.
