---
title: "Tuần 12"
date: 2026-07-06
weight: 12
chapter: false
pre: " <b> 1.12. </b> "
---

**Mục tiêu tuần:**
- Xây dựng ứng dụng báo cáo Streamlit hoạt động trên máy chủ ảo Amazon EC2.
- Tối ưu hóa các câu truy vấn cơ sở dữ liệu và cấu hình bộ nhớ đệm để tăng tốc độ hiển thị biểu đồ.
- Thiết lập cảnh báo AWS CloudWatch và thông báo SNS để theo dõi trạng thái hoạt động của quy trình dữ liệu.
- Soạn thảo tài liệu hướng dẫn triển khai song ngữ chi tiết và dọn dẹp toàn bộ tài nguyên đám mây để tránh phát sinh chi phí.

**Các công việc cần triển khai trong tuần này:**

| Thứ | Công việc | Ngày |
|---|---|---|
| Thứ Hai | Lập trình kịch bản Streamlit `app_beautiful.py` tích hợp các biểu đồ trực quan Plotly. Đẩy ứng dụng lên máy chủ EC2 và cấu hình các quy tắc bảo mật mạng để mở cổng truy cập. | 6/7 |
| Thứ Ba | Đo lường tốc độ phản hồi của trang và xử lý lỗi timeout khi gọi dữ liệu từ database. Cấu hình cơ chế cache bằng các hàm tích hợp của Streamlit để giảm thiểu tần suất gửi truy vấn SQL. | 7/7 |
| Thứ Tư | Thiết lập các cảnh báo lỗi trong CloudWatch dựa trên số lượng Glue job bị thất bại. Cấu hình dịch vụ SNS để tự động gửi thông báo qua email khi phát hiện sự cố. | 8/7 |
| Thứ Năm | Soạn thảo phần một tài liệu hướng dẫn chạy workshop bằng hai ngôn ngữ Anh - Việt. Viết chi tiết các bước cấu hình VPC, định cấu trúc bucket S3 và thiết lập danh mục dữ liệu Glue. | 9/7 |
| Thứ Sáu | Viết nốt phần hai tài liệu hướng dẫn về deploy máy chủ EC2, cấu hình giám sát và quy trình dọn dẹp hệ thống. Tiến hành xóa bỏ toàn bộ máy chủ, database và lưu trữ để tránh phát sinh chi phí. | 10/7 |

**Kết quả đạt được trong tuần là gì:**
- **Thứ Hai:**
  - Kết quả đạt được: Chạy thành công dashboard hiển thị các biểu đồ doanh thu và tương tác hoạt động trên EC2.
  - Bài học: Triển khai ứng dụng trên EC2 kết hợp thiết lập port bảo mật giúp tạo ra môi trường xem báo cáo độc lập và an toàn cho người dùng.
- **Thứ Ba:**
  - Kết quả đạt được: Giảm thời gian tải lại trang từ mười hai giây xuống dưới một giây nhờ lưu dữ liệu tạm thời.
  - Bài học: Sử dụng bộ nhớ đệm cache giúp ngăn ngừa việc quá tải số lượng kết nối tới database gốc và nâng cao trải nghiệm người dùng.
- **Thứ Tư:**
  - Kết quả đạt được: Hệ thống tự động gửi email cảnh báo khi giả lập lỗi chạy pipeline dữ liệu.
  - Bài học: Giám sát tự động giúp phát hiện lỗi vận hành ngay lập tức, hỗ trợ kỹ sư dữ liệu xử lý sự cố kịp thời.
- **Thứ Năm:**
  - Kết quả đạt được: Hoàn tất phần đầu tài liệu hướng dẫn cài đặt hệ thống chi tiết cho người học.
  - Bài học: Soạn thảo hướng dẫn chi tiết từng bước giúp học viên dễ dàng thực hành theo mà không gặp lỗi cấu hình hệ thống.
- **Thứ Sáu:**
  - Kết quả đạt được: Hoàn thành tài liệu, đẩy toàn bộ mã nguồn lên kho Git và xác nhận tài khoản AWS sạch tài nguyên.
  - Bài học: Tài liệu hóa quy trình dọn dẹp giúp học viên chủ động xóa bỏ tài nguyên sau khi kết thúc thực hành, tránh mất phí duy trì ngoài ý muốn.

