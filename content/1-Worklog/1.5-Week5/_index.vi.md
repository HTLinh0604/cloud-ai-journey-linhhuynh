---
title: "Tuần 5"
date: 2026-05-18
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

Mục tiêu tuần:
- Quản lý hiệu quả các dịch vụ cốt lõi (EC2, S3, IAM) thông qua AWS CLI.
- Triển khai quy trình tự động đồng bộ hóa dữ liệu từ local lên cloud.
- Xây dựng các quy tắc S3 Lifecycle để giảm thiểu tối đa chi phí lưu trữ đám mây.
- Thiết kế các chính sách sao lưu tự động cho các ổ đĩa block storage.

Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày |
|---|---|---|
| Thứ Hai | Thực hành các thao tác quản lý EC2, S3 và IAM sử dụng giao diện dòng lệnh. | 18/5 |
| Thứ Ba | Thiết lập đồng bộ hóa thư mục tự động lên S3 bằng lệnh copy và sync. | 19/5 |
| Thứ Tư | Triển khai chính sách S3 Lifecycle nhiều tầng để tự động chuyển đổi và xóa bỏ dữ liệu cũ. | 20/5 |
| Thứ Năm | Cấu hình EBS Data Lifecycle Manager để tự động tạo snapshot cho các volume production. | 21/5 |
| Thứ Sáu | Xác định các tham số lưu trữ snapshot và phân tích khung khôi phục thảm họa RTO/RPO. | 22/5 |

Kết quả đạt được trong tuần là gì:
- Sử dụng thành thạo các câu lệnh terminal để truy vấn nhanh và cấu hình hạ tầng đám mây.
- Thiết lập thành công các luồng đồng bộ tập tin cục bộ lên các bucket S3 từ xa.
- Tiết kiệm chi phí lưu trữ nhờ cấu hình tự động phân tầng cho các đối tượng cũ.
- Tự động hóa việc bảo vệ ổ đĩa hệ thống bằng các quy tắc snapshot EBS tự động.
