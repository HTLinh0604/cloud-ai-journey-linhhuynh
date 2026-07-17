---
title: "Tuần 2"
date: 2026-04-27
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

**Mục tiêu tuần:**
- Cấu hình Amazon S3 bucket với các tùy chọn nâng cao bao gồm versioning, mã hóa và lifecycle policies.
- Hiểu rõ các loại EBS volume, chỉ số hiệu năng và quản lý snapshot.
- Cấu hình EBS Data Lifecycle Manager (DLM) để tự động hóa lịch trình backup volume.
- Thiết lập cơ sở dữ liệu Amazon RDS an toàn trong các subnet tùy chỉnh.

**Các công việc cần triển khai trong tuần này:**

| Thứ | Công việc | Ngày |
|---|---|---|
| Thứ Hai | Tạo các bucket S3, bật versioning để theo dõi sao lưu và cấu hình mã hóa mặc định (SSE-S3). Thiết lập tính năng S3 Static Website Hosting để phục vụ trang index HTML đơn giản và kiểm tra chuyển hướng web. | 27/4 |
| Thứ Ba | Thiết lập S3 Lifecycle Policies để tự động chuyển đổi đối tượng nhằm tối ưu chi phí lưu trữ. Cấu hình quy tắc chuyển dữ liệu sang lớp Standard-IA sau 30 ngày và Glacier Deep Archive sau 90 ngày. | 28/4 |
| Thứ Tư | Phân tích các loại ổ đĩa EBS (gp3, io2, st1) tập trung vào các chỉ số IOPS và throughput. Tạo một ổ đĩa gp3 mới, gắn vào máy chủ EC2 đang hoạt động và tiến hành chụp snapshot thủ công. | 29/4 |
| Thứ Năm | Cấu hình Amazon Data Lifecycle Manager (DLM) để tự động hóa quy trình chụp snapshot. Định nghĩa chính sách backup hàng ngày với thời gian lưu trữ 7 ngày, nhắm mục tiêu vào các volume có gắn tag dự án. | 30/4 |
| Thứ Sáu | Khởi tạo instance Amazon RDS PostgreSQL (db.t3.micro) nằm trong DB Subnet Group của một custom VPC. Cấu hình security group chặn hoàn toàn truy cập public, chỉ cho phép nhận kết nối từ security group của ứng dụng EC2. | 1/5 |

**Kết quả đạt được trong tuần là gì:**
- **Thứ Hai:**
  - Kết quả đạt được: Cấu hình thành công S3 bucket có versioning và kiểm thử website tĩnh qua public endpoint.
  - Bài học: Tính năng versioning bảo vệ dữ liệu khỏi việc xóa nhầm bằng cách lưu lại các trạng thái cũ của tệp. Mã hóa mặc định giúp bảo vệ dữ liệu lưu trữ an toàn.
- **Thứ Ba:**
  - Kết quả đạt được: Cấu hình Lifecycle hoạt động trên bucket thử nghiệm và xác minh chính xác các quy tắc chuyển lớp.
  - Bài học: Tự động hóa vòng đời dữ liệu loại bỏ việc quản trị thủ công và giúp giảm đáng kể chi phí lưu trữ khi dữ liệu ít được truy cập dần theo thời gian.
- **Thứ Tư:**
  - Kết quả đạt được: Định dạng và mount thành công ổ đĩa gp3 vào EC2, đồng thời kiểm tra snapshot đã tạo.
  - Bài học: Ổ gp3 cho phép cấu hình độc lập giữa IOPS và throughput giúp tiết kiệm chi phí hơn so với dòng ổ gp2 thế hệ trước.
- **Thứ Năm:**
  - Kết quả đạt được: Chính sách DLM hoạt động ổn định và tự động chụp snapshot theo lịch trình.
  - Bài học: Tự động hóa sao lưu bằng DLM đảm bảo tính nhất quán của chính sách backup và tăng cường khả năng phục hồi khi gặp sự cố.
- **Thứ Sáu:**
  - Kết quả đạt được: Instance RDS chạy nội bộ an toàn, chặn mọi truy cập bên ngoài và kết nối thành công từ EC2 client.
  - Bài học: Ràng buộc truy cập database chỉ từ security group của ứng dụng là mô hình bảo mật chuẩn, ngăn chặn các rủi ro kết nối trái phép.

