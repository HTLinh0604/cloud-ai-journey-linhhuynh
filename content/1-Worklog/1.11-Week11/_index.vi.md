---
title: "Tuần 11"
date: 2026-06-29
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

**Mục tiêu tuần:**
- Viết script tạo dữ liệu khách hàng giả lập và khởi tạo các bucket lưu trữ S3.
- Lập trình các tác vụ Glue ETL bằng PySpark để xử lý dữ liệu qua các phân tầng Medallion.
- Cấu hình tự động đăng ký schema dữ liệu vào cơ sở dữ liệu Glue Data Catalog.
- Triển khai Athena workgroup và xác thực tính đúng đắn của các câu lệnh truy vấn báo cáo.

**Các công việc cần triển khai trong tuần này:**

| Thứ | Công việc | Ngày |
|---|---|---|
| Thứ Hai | Lập trình kịch bản Python tạo ra tệp tin ghi nhận hoạt động khách hàng giả lập dạng CSV. Khởi tạo các bucket S3 và dùng lệnh tải bộ dữ liệu lên phân vùng Raw. | 29/6 |
| Thứ Ba | Lập trình file `raw_to_bronze_job.py` bằng PySpark. Cấu hình chạy thử nghiệm tác vụ này trên AWS Glue để chuyển đổi kiểu dữ liệu và ghi định dạng Parquet nén Snappy. | 30/6 |
| Thứ Tư | Xây dựng file code `bronze_to_silver_job.py` thực hiện chuẩn hóa dữ liệu. Viết các phép biến đổi PySpark loại bỏ bản ghi trùng lặp và đồng bộ chữ hoa mã quốc gia. | 1/7 |
| Thứ Năm | Lập trình file `silver_to_gold_job.py` để tính toán các chỉ số nghiệp vụ KPI. Cấu hình Glue job tự động ghi dữ liệu vào S3 Gold và cập nhật cấu trúc bảng vào Data Catalog. | 2/7 |
| Thứ Sáu | Thiết lập cấu hình cho Athena workgroup và chỉ định vị trí xuất file kết quả. Thực hiện chạy thử nghiệm 7 câu lệnh truy vấn SQL để xác minh tính chính xác dữ liệu. | 3/7 |

**Kết quả đạt được trong tuần là gì:**
- **Thứ Hai:**
  - Kết quả đạt được: Tạo thành công bộ dữ liệu mười ngàn bản ghi và upload tệp tin an toàn lên hệ thống lưu trữ đám mây S3.
  - Bài học: Chủ động tạo dữ liệu mẫu chuẩn giúp kiểm tra tính ổn định của các bước phân tích cú pháp mà không cần phụ thuộc dữ liệu thật.
- **Thứ Ba:**
  - Kết quả đạt được: Tạo thành công Glue Job chuyển đổi tệp CSV thô thành tệp Parquet chuẩn hóa đặt tại phân vùng Bronze.
  - Bài học: Chuyển sang lưu trữ định dạng Parquet giúp tối ưu không gian lưu trữ và tăng tốc độ đọc dữ liệu khi truy vấn.
- **Thứ Tư:**
  - Kết quả đạt được: Tác vụ Glue Job làm sạch dữ liệu chạy ổn định, tạo ra phân vùng Silver sạch sẽ và chuẩn hóa.
  - Bài học: Loại bỏ trùng lặp tại tầng Silver giúp ngăn ngừa tình trạng tính toán sai lệch doanh thu ở các bước phân tích báo cáo sau này.
- **Thứ Năm:**
  - Kết quả đạt được: Glue Job tự động cập nhật bảng Gold đã tổng hợp dữ liệu và tự động đăng ký schema vào Glue Data Catalog.
  - Bài học: Tổng hợp dữ liệu tại Gold layer giúp tinh giản các truy vấn, hạn chế việc phải quét toàn bộ bảng khi kết nối báo cáo.
- **Thứ Sáu:**
  - Kết quả đạt được: Thực thi thành công 7 câu truy vấn nghiệp vụ với dung lượng quét của mỗi câu dưới năm mươi megabytes.
  - Bài học: Kết hợp phân vùng dữ liệu và lưu trữ cột dọc giúp giảm thiểu tối đa dung lượng dữ liệu cần quét, giữ chi phí ở mức tối ưu.

