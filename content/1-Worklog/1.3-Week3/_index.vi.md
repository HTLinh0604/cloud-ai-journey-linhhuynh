---
title: "Tuần 3"
date: 2026-05-04
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

**Mục tiêu tuần:**
- Cài đặt, cấu hình và sử dụng AWS CLI để quản lý tài nguyên bằng các bộ lọc truy vấn nâng cao.
- Hiểu rõ Amazon DynamoDB và các khái niệm thiết kế cơ sở dữ liệu NoSQL.
- Triển khai cache toàn cầu bằng CloudFront và tìm hiểu cấu hình Lambda@Edge.
- Xây dựng hạ tầng mạng tùy chỉnh với subnet công cộng và triển khai EC2 web server.
- Phát triển ứng dụng serverless với AWS Lambda và triển khai hạ tầng bằng AWS CDK.

**Các công việc cần triển khai trong tuần này:**

| Thứ | Công việc | Ngày |
|---|---|---|
| Thứ Hai (Lên văn phòng) | Cài đặt AWS CLI và cấu hình credentials. Thực hành viết câu lệnh truy vấn phức tạp dùng bộ lọc JMESPath. Thiết kế một custom VPC, subnet, route table, Internet Gateway và khởi chạy EC2 chạy Apache web server qua user data. | 4/5 |
| Thứ Ba (Lên văn phòng) | Khởi tạo bảng DynamoDB và nghiên cứu thiết kế partition key, sort key. Cấu hình phân phối Amazon CloudFront để cache các tài sản tĩnh và nghiên cứu cách Lambda@Edge can thiệp request ở biên. | 5/5 |
| Thứ Tư (Lên văn phòng) | Viết hàm Lambda bằng Python, cấu hình giới hạn ram và thời gian timeout. Khởi tạo một ứng dụng AWS CDK bằng TypeScript, viết code định nghĩa các construct S3 cơ bản. | 6/5 |
| Thứ Năm | Luyện tập câu lệnh CLI để đồng bộ hóa thư mục cục bộ lên bucket S3. Sử dụng các cờ cấu hình để lọc loại trừ tệp tin và thiết lập lớp lưu trữ trong quá trình tải lên. | 7/5 |
| Thứ Sáu | Cấu hình các quy tắc vòng đời S3 và xác minh điều kiện chuyển lớp dữ liệu. Sử dụng tiện ích AWS Toolkit trong VS Code để kết nối xem danh sách hàm Lambda và chạy thử truy vấn cục bộ. | 8/5 |

**Kết quả đạt được trong tuần là gì:**
- **Thứ Hai (Lên văn phòng):**
  - Kết quả đạt được: Cấu hình xong AWS CLI profiles, truy vấn nhanh danh sách instance và truy cập thành công Apache web page qua địa chỉ IP công cộng.
  - Bài học: Tự động hóa qua CLI giúp triển khai nhanh hơn console. Thiết kế VPC là lớp cô lập mạng cơ bản cho mọi tài nguyên đám mây.
- **Thứ Ba (Lên văn phòng):**
  - Kết quả đạt được: Bảng DynamoDB hoạt động có khóa chính composite, và phân phối CloudFront đã cache thành công các đối tượng từ origin.
  - Bài học: DynamoDB mở rộng quy mô ngang nhờ phân bổ khóa. Caching qua CloudFront giúp giảm tải cho origin và tăng tốc độ tải trang.
- **Thứ Tư (Lên văn phòng):**
  - Kết quả đạt được: Hàm Lambda hoạt động và CDK template biên dịch thành công ra tệp CloudFormation tương ứng.
  - Bài học: Lambda mang lại khả năng mở rộng serverless. CDK cho phép định nghĩa hạ tầng bằng mã nguồn lập trình tiêu chuẩn.
- **Thứ Năm:**
  - Kết quả đạt được: Viết script đồng bộ tệp cục bộ lên S3, kiểm tra mã hash tệp tin và liệt kê nội dung bucket bằng CLI.
  - Bài học: Viết kịch bản quản lý file S3 qua CLI là kỹ năng nền tảng cho việc tự động hóa các đường truyền backup dữ liệu sau này.
- **Thứ Sáu:**
  - Kết quả đạt được: Áp dụng thành công chính sách vòng đời dữ liệu S3 và kiểm thử chạy hàm Lambda cục bộ bằng IDE toolkit.
  - Bài học: Các công cụ tích hợp trong IDE giúp nâng cao năng suất lập trình nhờ khả năng gỡ lỗi nhanh trước khi deploy lên cloud.

