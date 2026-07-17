---
title: "Tuần 4"
date: 2026-05-11
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

**Mục tiêu tuần:**
- Sử dụng template AWS CloudFormation để xây dựng các stack hạ tầng tự động có khả năng lặp lại.
- Cấu hình AWS Glue Crawlers và quản lý siêu dữ liệu schema trong Data Catalog.
- Tối ưu hóa truy vấn Amazon Athena bằng định dạng tệp cột dọc.
- Cung cấp cơ sở dữ liệu RDS trong private subnet đi kèm các quy tắc bảo mật mạng.

**Các công việc cần triển khai trong tuần này:**

| Thứ | Công việc | Ngày |
|---|---|---|
| Thứ Hai | Viết template CloudFormation định nghĩa S3 bucket và IAM role. Thực hành quản lý stack qua CLI, tìm hiểu các phần mappings, parameter và xuất kết quả đầu ra. | 11/5 |
| Thứ Ba | Thiết lập AWS Glue Crawler để quét dữ liệu CSV thô trên S3. Cấu hình lịch chạy crawler và ánh xạ các trường dữ liệu trực tiếp vào cơ sở dữ liệu Glue Data Catalog. | 12/5 |
| Thứ Tư | Cấu hình Athena Workgroup và đặt giới hạn dung lượng quét để kiểm soát chi phí. Thực hành chạy các truy vấn SQL trên các bảng dữ liệu đã catalog. | 13/5 |
| Thứ Năm | Khởi tạo cơ sở dữ liệu Amazon RDS PostgreSQL nằm trong các private subnet của custom VPC. Cấu hình security group để giới hạn quyền kết nối chỉ từ máy chủ ứng dụng. | 14/5 |
| Thứ Sáu | Cấu hình Gateway VPC Endpoint cho S3 để cho phép các máy chủ trong private subnet truy cập S3 trực tiếp mà không cần đi qua Internet. Bật tính năng VPC Flow Logs để giám sát lưu lượng. | 15/5 |

**Kết quả đạt được trong tuần là gì:**
- **Thứ Hai:**
  - Kết quả đạt được: Triển khai thành công stack tài nguyên từ template CloudFormation và xác minh cấu hình qua CLI.
  - Bài học: CloudFormation mang lại nguồn cấu hình duy nhất cho hệ thống, đảm bảo tính nhất quán và dễ dàng tái triển khai.
- **Thứ Ba:**
  - Kết quả đạt được: Crawler hoạt động và tạo được bảng metadata trong Data Catalog với schema tự động nhận diện.
  - Bài học: Glue Crawler tự động hóa việc phát hiện cấu trúc dữ liệu, giữ cho siêu dữ liệu của catalog luôn đồng bộ với file lưu trữ vật lý.
- **Thứ Tư:**
  - Kết quả đạt được: Cấu hình workgroup có cảnh báo hạn mức, và thực thi các câu lệnh SQL trả về kết quả chính xác.
  - Bài học: Athena workgroup giúp phân chia tài nguyên và kiểm soát chi phí hiệu quả bằng cách giới hạn dung lượng quét tối đa của mỗi truy vấn.
- **Thứ Năm:**
  - Kết quả đạt được: Instance RDS chạy trong phân vùng private bảo mật và kết nối thành công từ môi trường được phân quyền.
  - Bài học: Đặt database trong private subnet ngăn chặn các nguy cơ tấn công mạng. Thiết lập SG hạn chế truy cập chỉ cho phép các dịch vụ hợp lệ kết nối.
- **Thứ Sáu:**
  - Kết quả đạt được: Cấu hình xong Gateway Endpoint cho S3 và xác minh luồng truy cập tệp nội bộ an toàn từ EC2.
  - Bài học: Gateway endpoint giữ cho luồng dữ liệu truyền tải nội bộ trong mạng AWS, giúp nâng cao tính bảo mật và tiết kiệm chi phí băng thông NAT.

