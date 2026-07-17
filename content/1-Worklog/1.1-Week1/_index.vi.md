---
title: "Tuần 1"
date: 2026-04-20
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---

**Mục tiêu tuần:**
- Kích hoạt tài khoản AWS và đảm bảo các promotional credits khởi đầu được áp dụng chính xác.
- Hoàn thành năm nhiệm vụ thực hành cốt lõi để khám phá kiến trúc compute, database và serverless.
- Nắm vững các khái niệm cơ bản về Điện toán đám mây, Hạ tầng toàn cầu và các biện pháp bảo mật.
- Thiết kế và triển khai chiến lược giám sát chi phí đa lớp cùng quy tắc gắn thẻ tài nguyên.

**Các công việc cần triển khai trong tuần này:**

| Thứ | Công việc | Ngày |
|---|---|---|
| Thứ Hai (Lên văn phòng) | Tạo tài khoản AWS mới, hoàn tất thiết lập thanh toán và kích hoạt 100 USD credit khởi đầu. Khởi chạy và kiểm tra một EC2 instance dùng key pair tự tạo, sử dụng Claude 3 Haiku playground trong Bedrock, cấu hình cảnh báo chi phí trong AWS Budgets, tạo hàm Lambda cơ bản, và cung cấp một cơ sở dữ liệu PostgreSQL trên RDS. | 20/4 |
| Thứ Ba | Nghiên cứu định nghĩa cốt lõi và lợi ích của Điện toán đám mây, phân biệt rõ các mô hình dịch vụ IaaS, PaaS, và SaaS. Phân tích hạ tầng toàn cầu của AWS bao gồm so sánh giữa Regions, Availability Zones, và Edge Locations về mặt độ trễ và tính sẵn sàng cao. | 21/4 |
| Thứ Tư (Lên văn phòng) | Cấu hình xác thực đa yếu tố (MFA) cho tài khoản root. Tạo các người dùng IAM, gán vào nhóm developers và administrators, đồng thời áp dụng phân quyền theo nguyên tắc đặc quyền tối thiểu. Thiết lập cảnh báo CloudWatch Billing tại các ngưỡng 25 USD, 50 USD và 75 USD kết hợp thông báo qua email của dịch vụ SNS. | 22/4 |
| Thứ Năm | Tìm hiểu sâu về các lớp lưu trữ của Amazon S3 (Standard, IA, Glacier, Deep Archive) và cơ chế độ bền dữ liệu 11 số chín. Phân tích các dòng EC2 instance (T3, M5, C5) để hiểu rõ cách phân bổ tài nguyên CPU, ram và băng thông mạng. | 23/4 |
| Thứ Sáu | Thực hành tạo bucket S3, tải lên tập tin và cấu hình quyền truy cập đối tượng. Khởi chạy máy chủ EC2 qua console, cấu hình security group mở các cổng cần thiết và thực hiện kết nối từ xa. | 24/4 |

**Kết quả đạt được trong tuần là gì:**
- **Thứ Hai (Lên văn phòng):**
  - Kết quả đạt được: Kích hoạt thành công tài khoản AWS với tổng cộng 200 USD credit khuyến mại. Toàn bộ năm tài nguyên thử nghiệm đã được khởi chạy và xóa bỏ an toàn.
  - Bài học: Làm quen trực quan với giao diện điều khiển AWS Console và xây dựng thói quen dọn dẹp tài nguyên thực hành ngay lập tức để tránh phát sinh chi phí.
- **Thứ Ba:**
  - Kết quả đạt được: Xây dựng tài liệu so sánh các mô hình dịch vụ đám mây và bản đồ phân bổ độ trễ theo vùng địa lý.
  - Bài học: Hiểu rõ việc lựa chọn region phù hợp là quyết định sống còn để giảm thiểu độ trễ truy cập, tuân thủ luật bảo vệ dữ liệu và đảm bảo dịch vụ hoạt động ổn định.
- **Thứ Tư (Lên văn phòng):**
  - Kết quả đạt được: Bảo mật thành công tài khoản root bằng MFA và thiết lập các tài khoản IAM phân quyền. Hệ thống cảnh báo chi phí đã kích hoạt và kiểm thử gửi email thành công.
  - Bài học: Bảo mật tài khoản root và phân quyền chi tiết qua IAM là nguyên tắc bảo mật cơ bản nhất trên cloud. Cảnh báo tự động giúp kiểm soát tốt ngân sách thử nghiệm.
- **Thứ Năm:**
  - Kết quả đạt được: Hoàn thành bảng đối chiếu tính năng, chi phí giữa các lớp lưu trữ S3 và các cấu hình dòng EC2.
  - Bài học: Việc lựa chọn đúng lớp lưu trữ S3 và dòng EC2 phù hợp với workload giúp tối ưu hóa tối đa chi phí vận hành mà vẫn đảm bảo hiệu năng hệ thống.
- **Thứ Sáu:**
  - Kết quả đạt được: Xác minh tệp tin tải lên S3 thành công và kết nối SSH thành công vào máy chủ EC2.
  - Bài học: Có trải nghiệm thực tế trong việc tự tay thiết lập tài nguyên và cấu hình bảo mật mạng thông qua security group.

