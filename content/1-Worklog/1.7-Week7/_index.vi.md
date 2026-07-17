---
title: "Tuần 7"
date: 2026-06-01
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

**Mục tiêu tuần:**
- Hiểu rõ các pattern thiết kế ETL analytics pipeline và kiến trúc Medallion trên AWS.
- Xây dựng data lake thử nghiệm kết hợp giữa S3, Glue và Athena.
- Tìm hiểu phương pháp phát triển Infrastructure-as-Code sử dụng CDK và CloudFormation.
- Thiết kế các workflow hướng sự kiện serverless sử dụng Step Functions và EventBridge.

**Các công việc cần triển khai trong tuần này:**

| Thứ | Công việc | Ngày |
|---|---|---|
| Thứ Hai | Phân tích kiến trúc dữ liệu Medallion, tìm hiểu vai trò và sự dịch chuyển dữ liệu giữa các tầng Raw, Bronze, Silver và Gold. Nghiên cứu chiến lược phân vùng đối tượng để tối ưu hóa việc tổ chức tệp tin trên S3. | 1/6 |
| Thứ Ba | Xây dựng mô hình data lake thử nghiệm trên S3. Thực hiện tải các tệp CSV thô lên, chạy Glue Crawler để tự động nhận dạng schema dữ liệu và chạy câu lệnh SQL để truy vấn bằng Athena. | 2/6 |
| Thứ Tư | Viết mã nguồn CDK định nghĩa tài nguyên S3 và IAM roles đi kèm. Thực hành biên dịch ứng dụng CDK ra CloudFormation nested templates và chạy lệnh deploy hệ thống. | 3/6 |
| Thứ Năm (Lên văn phòng) | Thiết lập workflow tự động hóa sử dụng dịch vụ điều phối AWS Step Functions. Xây dựng sơ đồ state machine có cấu hình các bước rẽ nhánh xử lý lỗi và định tuyến luồng đi của sự kiện qua EventBridge. | 4/6 |
| Thứ Sáu | Thực hiện ôn tập tổng hợp kiến thức về hệ thống mạng (subnets, route tables, gateway endpoints), lựa chọn cấu hình máy chủ và phân loại cơ sở dữ liệu để chuẩn bị xây dựng dự án cuối khóa. | 5/6 |

**Kết quả đạt được trong tuần là gì:**
- **Thứ Hai:**
  - Kết quả đạt được: Thiết kế cấu trúc thư mục lưu trữ data lake và quy tắc đặt tên thư mục phân vùng dựa theo mốc thời gian.
  - Bài học: Phân vùng dữ liệu đúng cách giúp định hình đường truyền dữ liệu sạch, đảm bảo các công cụ truy vấn sau này chỉ quét các tệp tin cần thiết.
- **Thứ Ba:**
  - Kết quả đạt được: Các bảng dữ liệu được đăng ký thành công trong Data Catalog và Athena thực thi truy vấn trích xuất dữ liệu chính xác.
  - Bài học: Bộ ba S3 + Glue + Athena tạo thành một hệ thống truy vấn mạnh mẽ, không tốn tài nguyên quản trị máy chủ và chi phí tối ưu theo lượng sử dụng.
- **Thứ Tư:**
  - Kết quả đạt được: Deploy thành công các thành phần hạ tầng thông qua việc biên dịch và chạy lệnh triển khai của CDK.
  - Bài học: Quản lý hạ tầng bằng code giúp chuẩn hóa các thiết kế tài nguyên, dễ dàng tích hợp vào các quy trình kiểm thử tự động.
- **Thứ Năm (Lên văn phòng):**
  - Kết quả đạt được: State machine hoạt động tốt, tự động chuyển đổi trạng thái công việc và EventBridge định tuyến sự kiện chính xác.
  - Bài học: Step Functions quản trị luồng xử lý serverless phức tạp một cách trực quan, giúp tăng cường tính tin cậy nhờ khả năng tự phục hồi lỗi.
- **Thứ Sáu:**
  - Kết quả đạt được: Bản vẽ sơ đồ mạng chi tiết và tài liệu hướng dẫn chọn lựa cấu hình tài nguyên cho dự án thực tế sắp tới.
  - Bài học: Nắm vững kiến thức nền tảng giúp đưa ra các quyết định thiết kế kiến trúc chuẩn xác, tối ưu hóa cả về mặt bảo mật lẫn chi phí.

