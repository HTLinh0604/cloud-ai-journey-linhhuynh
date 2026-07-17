---
title: "Tuần 10"
date: 2026-06-22
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

**Mục tiêu tuần:**
- Nghiên cứu các best practices trong Data Engineering bao gồm DataOps và kiểm soát schema drift.
- Tham gia sự kiện kỹ thuật tại văn phòng AWS để học hỏi kinh nghiệm tối ưu hóa chi phí thực chiến.
- Lập kế hoạch phân chia module code và phân bổ luồng công việc cho dự án.
- Cài đặt môi trường phát triển cục bộ và khởi tạo kho lưu trữ Git.

**Các công việc cần triển khai trong tuần này:**

| Thứ | Công việc | Ngày |
|---|---|---|
| Thứ Hai | Đọc tài liệu kỹ thuật về các nguyên lý DataOps và quản lý siêu dữ liệu. Phân tích các mô hình schema drift và phương pháp cô lập các trường dữ liệu lạ phát sinh trong pipeline. | 22/6 |
| Thứ Ba | Rà soát lại toàn bộ thiết kế kiến trúc của dự án. Xác định các định dạng phân vùng thư mục lưu trữ S3 và đảm bảo tính đồng nhất của siêu dữ liệu trên data catalog. | 23/6 |
| Thứ Tư | Tham gia sự kiện chia sẻ công nghệ tổ chức tại văn phòng Amazon Web Services. Lắng nghe các bài tham luận về tối ưu hóa chi phí dữ liệu lớn và trao đổi với các kỹ sư giải pháp. | 24/6 |
| Thứ Năm | Thiết lập tài liệu thiết kế phần mềm cho các kịch bản code xử lý. Chia nhỏ dự án thành các module độc lập, xác định các nhiệm vụ của Python và logic PySpark tương ứng. | 25/6 |
| Thứ Sáu | Khởi tạo môi trường ảo Python trên máy tính cá nhân. Cài đặt các thư viện PySpark cần thiết, cấu hình tài khoản dòng lệnh AWS CLI và tạo repository Git. | 26/6 |

**Kết quả đạt được trong tuần là gì:**
- **Thứ Hai:**
  - Kết quả đạt được: Xây dựng tài liệu kỹ thuật về phương án lưu trữ trường dữ liệu tự do vào cột định dạng JSON.
  - Bài học: Chủ động chuẩn bị phương án đối phó với schema drift giúp hệ thống vận hành liên tục, không bị sập khi dữ liệu đầu vào thay đổi cấu trúc.
- **Thứ Ba:**
  - Kết quả đạt được: Chốt sơ đồ thiết kế kiến trúc cuối cùng và khóa các tham số phân vùng đường dẫn S3.
  - Bài học: Thống nhất đường dẫn phân vùng từ đầu giúp đồng bộ cấu trúc thư mục lưu trữ vật lý với bảng ảo trên công cụ truy vấn.
- **Thứ Tư:**
  - Kết quả đạt được: Tích lũy tài liệu hướng dẫn kỹ thuật áp dụng tính năng partition projection để tối ưu hóa Athena.
  - Bài học: Học hỏi từ các tình huống thực tế của chuyên gia giúp tránh được các lỗi thiết kế phổ biến và học được giải pháp tối ưu chi phí.
- **Thứ Năm:**
  - Kết quả đạt được: Bản kế hoạch triển khai phần mềm chia rõ chức năng của từng file code xử lý.
  - Bài học: Phân rã mã nguồn thành các module nhỏ giúp dễ dàng kiểm tra tính đúng đắn của logic và thuận tiện khi làm việc nhóm.
- **Thứ Sáu:**
  - Kết quả đạt được: Thiết lập xong môi trường ảo, kiểm thử chạy thành công PySpark cục bộ và khởi tạo repo Git.
  - Bài học: Môi trường phát triển cục bộ chuẩn hóa giúp lập trình viên thử nghiệm code nhanh chóng, an toàn trước khi đẩy lên cloud.

