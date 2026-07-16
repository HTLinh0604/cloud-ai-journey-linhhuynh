---
title: "Tuần 6"
date: 2026-05-25
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

Mục tiêu tuần:
- Xây dựng các pipeline cơ sở dữ liệu hướng sự kiện bằng DynamoDB Streams.
- Tìm hiểu tính năng sao chép đa vùng qua DynamoDB Global Tables.
- Nghiên cứu kiến trúc bộ nhớ đệm cache sử dụng DynamoDB Accelerator (DAX).
- Phân tích cấu hình tính sẵn sàng cao Multi-AZ và hành vi failover của Amazon RDS.
- Thực hiện so sánh kỹ thuật giữa hai giải pháp cơ sở dữ liệu NoSQL và SQL.

Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày |
|---|---|---|
| Thứ Hai | Triển khai Lambda trigger để xử lý sự kiện thời gian thực từ các thay đổi của DynamoDB Streams. | 25/5 |
| Thứ Ba | Học về cơ chế sao chép active-active của DynamoDB Global Tables. | 26/5 |
| Thứ Tư | Tìm hiểu cấu hình DynamoDB Accelerator (DAX) và đánh giá các lựa chọn giữa DAX và ElastiCache. | 27/5 |
| Thứ Năm | Nghiên cứu sâu về triển khai RDS Multi-AZ, các read replica và quy tắc lưu trữ bản sao lưu. | 28/5 |
| Thứ Sáu | Đánh giá và lập tài liệu so sánh trade-off giữa SQL và NoSQL cho các bài toán thực tế. | 29/5 |

Kết quả đạt được trong tuần là gì:
- Xây dựng thành công các serverless function xử lý thay đổi dữ liệu theo thời gian thực.
- Nắm vững kiến thức về kiến trúc cơ sở dữ liệu phân tán toàn cầu và cấu hình hoạt động song song.
- Hiểu rõ phương pháp tăng tốc độ đọc dữ liệu và giảm tải cơ sở dữ liệu bằng bộ nhớ đệm DAX.
- Xây dựng khung quyết định chặt chẽ để chọn lựa hệ quản trị cơ sở dữ liệu dựa trên các tiêu chí mở rộng và tính nhất quán.
