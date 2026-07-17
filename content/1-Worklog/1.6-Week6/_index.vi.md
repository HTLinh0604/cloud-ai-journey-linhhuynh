---
title: "Tuần 6"
date: 2026-05-25
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

**Mục tiêu tuần:**
- Hiểu rõ DynamoDB Streams và cấu hình Lambda trigger phục vụ cho kiến trúc cơ sở dữ liệu hướng sự kiện.
- Phân tích cấu hình DynamoDB Global Tables phục vụ sao chép active-active đa vùng.
- Cấu hình DynamoDB Accelerator (DAX) caching để giảm độ trễ truy vấn đọc dữ liệu.
- Quản lý cấu hình RDS Multi-AZ và đánh giá khả năng mở rộng của cơ sở dữ liệu quan hệ.

**Các công việc cần triển khai trong tuần này:**

| Thứ | Công việc | Ngày |
|---|---|---|
| Thứ Hai | Tìm hiểu cơ chế hoạt động của DynamoDB Streams và các định dạng bản ghi (INSERT, MODIFY, REMOVE). Thiết lập hàm Lambda để bắt các sự kiện thay đổi dữ liệu từ stream. | 25/5 |
| Thứ Ba | Tìm hiểu cơ chế đồng bộ dữ liệu của DynamoDB Global Tables. Cấu hình bảng hoạt động song song tại hai region khác nhau và kiểm tra độ trễ đồng bộ dữ liệu giữa hai vùng. | 26/5 |
| Thứ Tư | Khởi tạo cụm cache DynamoDB Accelerator (DAX). Cấu hình client kết nối qua endpoint của DAX để đo lường sự thay đổi về tốc độ phản hồi truy vấn đọc. | 27/5 |
| Thứ Năm | Nghiên cứu tính năng RDS Multi-AZ và Read Replica. Thực hiện giả lập tình huống lỗi để kiểm tra quy trình failover tự động và đánh giá khả năng phân tải đọc của Read Replica. | 28/5 |
| Thứ Sáu | Thực hiện so sánh toàn diện giữa cơ sở dữ liệu quan hệ (SQL) và phi quan hệ (NoSQL). Đối chiếu chi tiết các khía cạnh về schema, khả năng query, khả năng scale và tính toàn vẹn dữ liệu. | 29/5 |

**Kết quả đạt được trong tuần là gì:**
- **Thứ Hai:**
  - Kết quả đạt được: Kích hoạt thành công stream trên bảng DynamoDB và cấu hình Lambda trigger ghi lại lịch sử thay đổi vào CloudWatch.
  - Bài học: DynamoDB Streams cho phép xây dựng ứng dụng phản hồi theo thời gian thực dựa trên các thay đổi dữ liệu mà không cần chạy vòng lặp truy vấn liên tục.
- **Thứ Ba:**
  - Kết quả đạt được: Bảng Global Table hoạt động ổn định, ghi nhận dữ liệu cập nhật đồng thời ở các vùng địa lý.
  - Bài học: Global Tables giải quyết bài toán độ trễ truy cập cho người dùng toàn cầu và cung cấp phương án DR dự phòng nóng cực kỳ tin cậy.
- **Thứ Tư:**
  - Kết quả đạt được: Cụm cache DAX hoạt động chính xác giúp giảm thời gian phản hồi câu lệnh đọc dữ liệu.
  - Bài học: DAX giúp giảm độ trễ truy cập đọc từ hàng millisecond xuống hàng microsecond, bảo vệ database gốc khỏi quá tải khi số lượng truy vấn đọc tăng vọt.
- **Thứ Năm:**
  - Kết quả đạt được: Quy trình chuyển đổi dự phòng Multi-AZ hoạt động tốt và Read Replica phân luồng tải đọc dữ liệu thành công.
  - Bài học: Multi-AZ hướng tới tính sẵn sàng cao của hệ thống, trong khi Read Replica hướng tới việc tối ưu hóa hiệu năng truy vấn cho các tác vụ báo cáo.
- **Thứ Sáu:**
  - Kết quả đạt được: Xây dựng tài liệu hướng dẫn chọn lựa giải pháp lưu trữ phù hợp cho các bài toán nghiệp vụ khác nhau.
  - Bài học: Lựa chọn loại database cần dựa trên cấu trúc dữ liệu và mô hình truy vấn: SQL tối ưu cho quan hệ phức tạp; NoSQL tối ưu cho tốc độ và mở rộng quy mô.

