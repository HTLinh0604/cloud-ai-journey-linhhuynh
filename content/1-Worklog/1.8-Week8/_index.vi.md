---
title: "Tuần 8"
date: 2026-06-08
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

Mục tiêu tuần:
- Khám phá việc giả lập môi trường AWS cục bộ sử dụng LocalStack và Floci.
- Nghiên cứu các mô hình kỹ nghệ dữ liệu hiện đại và kiến trúc Medallion.
- Thiết kế hệ thống cho pipeline dữ liệu của dự án cuối khóa.
- Xây dựng một nguyên mẫu xử lý dữ liệu cục bộ bằng PySpark.
- Phân tích vai trò vận hành của các thành phần trong pipeline.

Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày |
|---|---|---|
| Thứ Hai | Cấu hình LocalStack và Floci để giả lập cục bộ các dịch vụ S3, Lambda và DynamoDB. | 8/6 |
| Thứ Ba | Tìm hiểu về các tầng chất lượng Medallion, sự tiến hóa schema và khả năng quan sát pipeline. | 9/6 |
| Thứ Tư | Thiết kế kiến trúc tổng thể cho pipeline dữ liệu và lựa chọn các dịch vụ AWS tích hợp. | 10/6 |
| Thứ Năm | Phát triển nguyên mẫu đầu cuối cục bộ sử dụng dữ liệu giả lập và mã chuyển đổi PySpark. | 11/6 |
| Thứ Sáu | Phân tích chi tiết vai trò của các tầng thu nhận, lưu trữ và xử lý trong hệ thống. | 12/6 |

Kết quả đạt được trong tuần là gì:
- Thiết lập thành công khung kiểm thử và phát triển AWS cục bộ để tối ưu hóa chi phí.
- Định hình rõ nét kiến trúc Medallion của dự án sử dụng Firehose, Glue và Athena.
- Xác thực thành công logic của các đoạn mã xử lý dữ liệu qua nguyên mẫu PySpark cục bộ.
- Hoàn thành bản đồ ánh xạ schema dữ liệu và các vị trí lưu trữ trên các tầng chất lượng.
