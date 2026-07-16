---
title: "Tuần 11"
date: 2026-06-29
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

Mục tiêu tuần:
- Xây dựng script Python để giả lập các sự kiện tương tác của khách hàng.
- Triển khai các bucket S3 và cấu hình các chính sách truy cập an toàn.
- Thiết lập Glue ETL job đầu tiên để đưa dữ liệu thô vào tầng Bronze.
- Tạo Glue ETL job thứ hai phục vụ làm sạch và chuẩn hóa dữ liệu.
- Phát triển Glue ETL job thứ ba để tổng hợp KPI vào các bảng Gold và tự động đăng ký với Glue Catalog.
- Cấu hình Athena workgroups và chạy xác thực các truy vấn phân tích nghiệp vụ.

Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày |
|---|---|---|
| Thứ Hai | Triển khai script sinh dữ liệu sự kiện giả lập và cấu hình bảo mật cho các bucket S3. | 29/6 |
| Thứ Ba | Tạo và chạy thử Glue ETL job chuyển đổi từ raw sang bronze với việc chuẩn hóa schema. | 30/6 |
| Thứ Tư | Thiết lập Glue job chuyển đổi từ bronze sang silver để loại bỏ trùng lặp và chuẩn hóa dữ liệu. | 1/7 |
| Thứ Năm | Triển khai Glue job từ silver sang gold để tổng hợp dữ liệu nghiệp vụ và đồng bộ với Data Catalog. | 2/7 |
| Thứ Sáu | Thiết lập Athena Workgroups với giới hạn dung lượng quét và thực thi các truy vấn kiểm thử. | 3/7 |

Kết quả đạt được trong tuần là gì:
- Thiết lập thành công cấu trúc phân tầng lưu trữ và tạo 10.000 sự kiện giả lập.
- Xây dựng và khởi chạy thành công ba Glue ETL job viết bằng PySpark.
- Đăng ký trực tiếp các bảng phân tích tầng Gold vào Glue Data Catalog.
- Xác thực thành công logic các truy vấn nghiệp vụ trên Athena trong giới hạn chi phí cho phép.
- Tiết kiệm chi phí triển khai nhờ bỏ qua việc chạy Crawler và cập nhật trực tiếp metadata thông qua dynamic frame.
