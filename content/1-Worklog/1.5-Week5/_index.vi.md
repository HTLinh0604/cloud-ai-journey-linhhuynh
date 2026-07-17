---
title: "Tuần 5"
date: 2026-05-18
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

**Mục tiêu tuần:**
- Viết các kịch bản lệnh bash chứa câu lệnh AWS CLI để thực hiện các thao tác quản trị trên EC2, S3 và IAM.
- Triển khai giải pháp đồng bộ hóa thư mục thời gian thực từ các máy cục bộ lên dịch vụ lưu trữ Amazon S3.
- Xây dựng quy tắc vòng đời S3 Lifecycle Policies để tự động chuyển đổi các phân lớp lưu trữ dựa trên tuổi thọ đối tượng.
- Triển khai các quy tắc quản lý snapshot tự động sử dụng Amazon Data Lifecycle Manager nhằm đạt mục tiêu khôi phục dữ liệu.

**Các công việc cần triển khai trong tuần này:**

| Thứ | Công việc | Ngày |
|---|---|---|
| Thứ Hai | Tự động hóa việc cấp phát máy chủ ảo và kiểm tra thông tin truy cập bằng các kịch bản bash sử dụng AWS CLI. Xây dựng các truy vấn lọc để trích xuất thông tin chi tiết các thực thể đang hoạt động. | 18/5 |
| Thứ Ba | Triển khai các quy trình tự động sử dụng lệnh đồng bộ để sao lưu các thư mục từ máy cục bộ lên S3. Kiểm tra tính toàn vẹn của dữ liệu bằng cách so sánh mã kiểm tra của tệp sau khi hoàn thành. | 19/5 |
| Thứ Tư | Thiết lập cấu hình vòng đời dữ liệu S3 Lifecycle Policies thông qua các tệp quy tắc cấu trúc XML. Định nghĩa thời hạn để tự động chuyển các tệp dữ liệu sang lớp Glacier Instant Retrieval sau ba mươi ngày. | 20/5 |
| Thứ Năm | Cấu hình lịch trình tự động tạo bản sao lưu snapshot cho các ổ đĩa EBS quan trọng thông qua Data Lifecycle Manager. Xác định khung thời gian thực hiện và gắn thẻ tài nguyên đích để áp dụng quy tắc. | 21/5 |
| Thứ Sáu | Tính toán các chỉ số về thời gian khôi phục và điểm khôi phục dựa trên tần suất chụp snapshot thực tế của ổ đĩa. Dọn dẹp các bản snapshot thử nghiệm đã hết hạn nhằm tối ưu hóa chi phí lưu trữ tài khoản. | 22/5 |

**Kết quả đạt được trong tuần là gì:**
- **Thứ Hai:**
  - Kết quả đạt được: Triển khai thành công máy chủ EC2 và cấu hình thông tin người dùng IAM hoàn toàn qua terminal.
  - Bài học: Việc đóng gói các câu lệnh CLI thành script giúp chuẩn hóa quy trình deploy hạ tầng, tránh các sai sót so với cấu hình thủ công.
- **Thứ Ba:**
  - Kết quả đạt được: Kịch bản chạy đồng bộ thư mục lên S3 hoạt động ổn định, tự động gán phân lớp lưu trữ thích hợp cho tệp tin.
  - Bài học: Lệnh đồng bộ hóa thông minh chỉ truyền tải các phần dữ liệu thay đổi giúp tối ưu hóa dung lượng truyền và tiết kiệm tài nguyên mạng.
- **Thứ Tư:**
  - Kết quả đạt được: Quy tắc S3 Lifecycle hoạt động trên các bucket chỉ định giúp chuyển đổi lớp lưu trữ tự động.
  - Bài học: Chuyển dữ liệu ít dùng sang lớp lưu trữ giá rẻ là phương án tối ưu FinOps tối thiểu chi phí lưu trữ đáng kể cho tổ chức.
- **Thứ Năm:**
  - Kết quả đạt được: Thiết lập thành công chính sách DLM tự động chụp snapshot ổ đĩa định kỳ hàng ngày.
  - Bài học: Thiết lập chính sách backup qua DLM giúp đảm bảo an toàn thông tin hệ thống, phòng ngừa rủi ro hỏng hóc thiết bị vật lý.
- **Thứ Sáu:**
  - Kết quả đạt được: Hoàn thành tài liệu quy trình khôi phục thảm họa và xác minh phục hồi thành công dữ liệu từ snapshot thử nghiệm.
  - Bài học: Quy trình sao lưu chỉ thực sự có giá trị khi hoạt động khôi phục được thử nghiệm và chứng minh hoạt động ổn định.

