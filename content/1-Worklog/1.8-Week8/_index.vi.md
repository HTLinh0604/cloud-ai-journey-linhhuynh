---
title: "Tuần 8"
date: 2026-06-08
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

**Mục tiêu tuần:**
- Thiết lập môi trường phát triển và kiểm thử cục bộ sử dụng LocalStack và Floci để mô phỏng các dịch vụ đám mây AWS.
- Nghiên cứu các mô hình kỹ thuật dữ liệu hiện đại bao gồm các tầng chất lượng trong kiến trúc Medallion và giám sát pipeline.
- Thiết kế kiến trúc data pipeline cho dự án cuối khóa và lựa chọn các dịch vụ tích hợp phù hợp.
- Phát triển kịch bản biến đổi dữ liệu mẫu cục bộ sử dụng công cụ xử lý PySpark.
- Tài liệu hóa trách nhiệm vận hành của từng thành phần trong pipeline dữ liệu dự án.

**Các công việc cần triển khai trong tuần này:**

| Thứ | Công việc | Ngày |
|---|---|---|
| Thứ Hai | Cài đặt và cấu hình LocalStack trên máy tính phát triển. Thiết lập công cụ Floci để mô phỏng dịch vụ lưu trữ S3 và môi trường thực thi AWS Lambda cục bộ. | 8/6 |
| Thứ Ba | Nghiên cứu thiết kế dữ liệu Medallion để hiểu cách chuyển đổi dữ liệu qua các tầng Bronze, Silver và Gold. Định nghĩa cơ chế xác thực schema dữ liệu đầu vào. | 9/6 |
| Thứ Tư | Thiết kế kiến trúc tổng quan của data pipeline dự án. Lựa chọn các dịch vụ tích hợp bao gồm Kinesis Data Firehose để truyền dữ liệu và Glue cho các tác vụ ETL. | 10/6 |
| Thứ Năm | Viết script xử lý PySpark cục bộ để làm sạch dữ liệu khách hàng giả lập. Thử nghiệm logic phân tích cú pháp dữ liệu bằng môi trường spark cục bộ. | 11/6 |
| Thứ Sáu | Tạo tài liệu đặc tả kỹ thuật mô tả vai trò của S3, Glue và Athena trong hệ thống. Ánh xạ các schema siêu dữ liệu cho từng giai đoạn chuyển đổi dữ liệu. | 12/6 |

**Kết quả đạt được trong tuần là gì:**
- **Thứ Hai:**
  - Kết quả đạt được: Xác minh tính năng tạo bucket S3 và kiểm tra tải tệp tin cục bộ thông qua emulator.
  - Bài học: Trình mô phỏng cung cấp môi trường thử nghiệm miễn phí giúp kiểm tra logic hạ tầng trước khi deploy thực tế.
- **Thứ Ba:**
  - Kết quả đạt được: Hoàn thành tài liệu nghiên cứu về sự tiến hóa của schema và các chiến lược kiểm tra dữ liệu đầu vào.
  - Bài học: Thiết kế cơ chế xác thực schema ngăn chặn các bản ghi lỗi làm hỏng dữ liệu phân tích ở các tầng sau.
- **Thứ Tư:**
  - Kết quả đạt được: Hoàn thành sơ đồ kiến trúc chi tiết mô tả đường đi của dữ liệu từ ingestion đến analytics.
  - Bài học: Vẽ sơ đồ hệ thống giúp phát hiện các điểm nghẽn tiềm ẩn và thống nhất hiểu biết của cả đội ngũ về dự án.
- **Thứ Năm:**
  - Kết quả đạt được: Chạy thành công tác vụ PySpark chuyển đổi dữ liệu CSV thô sang tệp tin Parquet nén Snappy.
  - Bài học: Kiểm thử PySpark cục bộ giúp đảm bảo logic biến đổi đúng đắn trước khi chạy các tác vụ Glue đắt đỏ trên cloud.
- **Thứ Sáu:**
  - Kết quả đạt được: Hoàn tất tài liệu ánh xạ cấu trúc dữ liệu và các yêu cầu chất lượng cho từng phân vùng dữ liệu.
  - Bài học: Tài liệu kỹ thuật đảm bảo pipeline được xây dựng đúng thiết kế và là cẩm nang tra cứu khi lập trình.

