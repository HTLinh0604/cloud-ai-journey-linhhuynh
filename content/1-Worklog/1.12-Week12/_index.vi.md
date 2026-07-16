---
title: "Tuần 12"
date: 2026-07-06
weight: 12
chapter: false
pre: " <b> 1.12. </b> "
---

Mục tiêu tuần:
- Xây dựng và triển khai dashboard phân tích Streamlit lên EC2 instance.
- Kiểm thử, sửa lỗi và tối ưu hóa thời gian tải của dashboard.
- Cấu hình các cảnh báo số liệu CloudWatch và dashboard theo dõi sức khỏe pipeline.
- Biên soạn tài liệu hướng dẫn workshop song ngữ và dọn dẹp các tài nguyên AWS đã triển khai.

Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày |
|---|---|---|
| Thứ Hai | Triển khai ứng dụng phân tích Streamlit và khởi chạy trên một instance EC2. | 6/7 |
| Thứ Ba | Kiểm thử các thành phần biểu đồ, xử lý lỗi timeout truy vấn và tích hợp bộ nhớ đệm cache. | 7/7 |
| Thứ Tư | Thiết lập các cảnh báo CloudWatch cho lỗi của Glue job và thiết kế dashboard giám sát. | 8/7 |
| Thứ Năm | Soạn thảo phần một hướng dẫn thực hành song ngữ bao gồm VPC, S3, Glue và Athena. | 9/7 |
| Thứ Sáu | Soạn thảo phần hai hướng dẫn song ngữ về EC2, hệ thống giám sát và quy trình giải phóng tài nguyên. | 10/7 |

Kết quả đạt được trong tuần là gì:
- Khởi chạy thành công dashboard phân tích dữ liệu trực quan dùng Streamlit và Plotly trên máy chủ EC2.
- Rút ngắn thời gian tải trang từ 12 giây xuống dưới 1 giây nhờ tích hợp cơ chế cache dữ liệu.
- Thiết lập thông báo tự động khi pipeline gặp lỗi qua CloudWatch và SNS.
- Hoàn thành bộ tài liệu hướng dẫn song ngữ chi tiết từng bước thiết lập và dọn dẹp cho người học.
- Dọn dẹp triệt để các tài nguyên database, máy chủ và lưu trữ để tránh phát sinh chi phí phát sinh.
