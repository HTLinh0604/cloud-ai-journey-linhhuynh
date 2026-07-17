---
title: "Tuần 9"
date: 2026-06-15
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

**Mục tiêu tuần:**
- Hoàn thiện bản thiết kế kiến trúc tổng thể và chi tiết hóa tích hợp giữa các thành phần.
- Phân tích và tính toán chi phí hàng tháng ước tính cho toàn bộ tài nguyên bằng AWS Pricing Calculator.
- Xác định các thông số kỹ thuật về khả năng mở rộng, khả năng chịu lỗi và bảo mật cho pipeline.
- Tài liệu hóa các đánh giá trade-off dịch vụ và chuẩn bị lưu đồ kỹ thuật cho workshop.

**Các công việc cần triển khai trong tuần này:**

| Thứ | Công việc | Ngày |
|---|---|---|
| Thứ Hai | Xác định các lớp của kiến trúc Medallion, lập bản đồ trạng thái dữ liệu từ tệp tin CSV thô sang các bảng Parquet tổng hợp trong phân vùng Gold. Định nghĩa cấu trúc bucket S3 cho từng tầng chất lượng dữ liệu. | 15/6 |
| Thứ Ba | Nghiên cứu các giải pháp thu thập dữ liệu luồng, so sánh Kinesis Data Firehose với Apache Kafka. Tìm hiểu về mô hình Change Data Capture (CDC) để đồng bộ hóa dữ liệu từ database nghiệp vụ lên data lake. | 16/6 |
| Thứ Tư | Sử dụng công cụ AWS Pricing Calculator để tính toán chi phí vận hành hàng tháng của S3, Glue ETL, Athena và EC2. Đề xuất các phương án tối ưu hóa chi phí. | 17/6 |
| Thứ Năm | Thiết kế các yêu cầu bảo mật bao gồm ma trận phân quyền IAM áp dụng đặc quyền tối thiểu. Định nghĩa chính sách mã hóa dữ liệu trên S3 và cấu hình cơ chế tự động chạy lại cho các tác vụ Glue. | 18/6 |
| Thứ Sáu | Vẽ lưu đồ kỹ thuật biểu diễn luồng đi của dữ liệu. Hoàn thành tài liệu đánh giá trade-off, quyết định lựa chọn Firehose, Glue và Athena để tối giản hóa kiến trúc và giảm chi phí đầu tư. | 19/6 |

**Kết quả đạt được trong tuần là gì:**
- **Thứ Hai:**
  - Kết quả đạt được: Chốt cấu trúc cây thư mục S3 và ánh xạ sự thay đổi cấu trúc dữ liệu qua từng tầng lọc.
  - Bài học: Thiết kế chặt chẽ cấu trúc thư mục giúp ngăn chặn sự hỗn loạn của siêu dữ liệu và tránh các lỗi phân tích cú pháp khi crawl dữ liệu.
- **Thứ Ba:**
  - Kết quả đạt được: Hoàn thành tài liệu đánh giá tính năng và chi phí giữa Kinesis và Kafka.
  - Bài học: Kinesis Firehose được tích hợp sâu vào hệ sinh thái AWS giúp giảm đáng kể thời gian lập trình và vận hành so với việc tự duy trì cụm Kafka.
- **Thứ Tư:**
  - Kết quả đạt được: Báo cáo chi phí chi tiết chỉ ra các khoản tiêu hao tài nguyên đám mây và số tiền tiết kiệm được khi chuyển sang Parquet.
  - Bài học: Định dạng lưu trữ dạng cột như Parquet giảm lượng dữ liệu cần quét, giúp tiết kiệm đến 85% chi phí vận hành truy vấn Athena.
- **Thứ Năm:**
  - Kết quả đạt được: Hoàn tất bộ chính sách phân quyền cho các dịch vụ và các tham số cấu hình chịu lỗi cho pipeline.
  - Bài học: Áp dụng quyền truy cập chặt chẽ thông qua IAM role giúp bảo vệ an toàn cho dữ liệu lưu trữ, ngăn ngừa rò rỉ thông tin.
- **Thứ Sáu:**
  - Kết quả đạt được: Hoàn thiện tài liệu kỹ thuật và checklist chuẩn bị cho giai đoạn lập trình dự án thực tế.
  - Bài học: Ghi chép rõ ràng lý do lựa chọn công nghệ giúp ích cho việc nâng cấp hệ thống sau này và định hướng cho đội ngũ triển khai.

