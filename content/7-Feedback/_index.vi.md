---
title: "Chia sẻ và Phản hồi"
date: 2024-01-01
weight: 7
chapter: false
pre: " <b> 7. </b> "
---

# Chia sẻ và Phản hồi

> *Phần này chia sẻ cảm nhận cá nhân và phản hồi thành thật của tôi về chương trình **First Cloud AI Journey (FCAJ)**. Hy vọng những suy nghĩ này có ích cho đội ngũ FCJ và những người tham gia trong tương lai.*

---

## 1. Cảm nhận về chương trình

Tham gia FCAJ là một trong những trải nghiệm có giá trị thực tiễn nhất tôi có được trong hành trình học cloud. Khác với các khóa học online thông thường nơi bạn chỉ làm theo demo được cấu hình sẵn, FCAJ đẩy tôi phải xây dựng thứ gì đó thực sự từ đầu - thiết kế kiến trúc, viết code, debug lỗi thật sự, và ghi lại từng bước.

Cấu trúc chương trình được thiết kế rất kỹ lưỡng: đưa ra đủ hướng dẫn để người tham gia không bị lạc hoàn toàn, nhưng vẫn để đủ không gian để chúng tôi tự ra quyết định và học từ những hậu quả đó. Sự cân bằng đó - có cấu trúc nhưng vẫn mở - chính là điều làm cho trải nghiệm thực sự mang tính giáo dục chứ không chỉ là một tutorial có hướng dẫn.

Với tư cách nhóm trưởng, tôi còn đạt được những kỹ năng vượt ra ngoài kỹ thuật: tôi học cách phối hợp những người có mức độ kinh nghiệm khác nhau, cách giao tiếp về ưu tiên khi chịu áp lực thời gian, và cách giữ tinh thần nhóm khi mọi thứ không diễn ra như mong đợi.

---

## 2. Mức độ hài lòng

**Mức hài lòng tổng thể: ⭐⭐⭐⭐ (4/5)**

| Khía cạnh | Hài lòng | Ghi chú |
|-----------|----------|---------|
| Độ sâu kỹ thuật của nội dung | ⭐⭐⭐⭐⭐ | Xuất sắc - dịch vụ AWS thực tế, kiến trúc thực tế, debug thực tế |
| Cấu trúc & hướng dẫn chương trình | ⭐⭐⭐⭐⭐ | Rõ ràng và vừa phải; một số bước có thể thêm screenshot ví dụ |
| Hỗ trợ từ mentor/admin | ⭐⭐⭐⭐⭐ | Phản hồi nhanh và hữu ích; tôi đánh giá cao văn hóa Q&A thoải mái |
| Mức độ liên quan đến công việc thực tế | ⭐⭐⭐⭐⭐ | Rất cao - mô hình Medallion Lakehouse là chuẩn của ngành |
| Phân bổ thời gian | ⭐⭐⭐ | Một số phần cảm giác hơi vội; cần thêm thời gian cho bước ETL và monitoring |

---

## 3. Điểm cần cải thiện

Dù trải nghiệm tổng thể của tôi rất tích cực, tôi có một vài gợi ý mang tính xây dựng cho đội ngũ FCJ:

**a) Giới thiệu khái niệm FinOps sớm hơn từ đầu**
Khía cạnh tối ưu chi phí của kiến trúc (Parquet, Athena workgroups, Glue DPU sizing) rất thú vị nhưng được giới thiệu khá muộn. Nếu người tham gia hiểu lý do cost từ ban đầu, họ sẽ đưa ra các quyết định thiết kế tốt hơn trong suốt quá trình.

**b) Tùy chọn môi trường "starter" có sẵn**
Thiết lập VPC, IAM roles và S3 bucket từ đầu tốn khá nhiều thời gian ở giai đoạn đầu. Cung cấp một template CloudFormation/Terraform tùy chọn cho những người muốn tập trung vào phần data engineering sẽ hữu ích - không bắt buộc, để giữ nguyên giá trị học tập.

**c) Hướng dẫn troubleshooting có cấu trúc hơn**
Khi Glue job thất bại hoặc truy vấn Athena không trả về kết quả, người tham gia lần đầu có thể cảm thấy bị choáng ngợp. Một trang tham khảo "Các vấn đề thường gặp & Cách debug" chuyên biệt trong tài liệu workshop sẽ giảm đáng kể sự bức bí.

**d) Phiên đánh giá chéo giữa các nhóm**
Thêm một phiên ngắn để các nhóm trình bày kiến trúc của mình cho nhau và nhận phản hồi sẽ tạo ra trải nghiệm học tuyệt vời, đồng thời khuyến khích các cách tiếp cận khác nhau cho cùng một vấn đề.

---

## 4. Có giới thiệu chương trình cho bạn bè không? Vì sao?

**Có, chắc chắn rồi - và tôi đã làm vậy rồi.**

Tôi sẽ giới thiệu FCAJ cho:

- **Sinh viên và developer mới vào nghề** đã học lý thuyết AWS nhưng chưa từng tự xây dựng một kiến trúc hoàn chỉnh, giống môi trường production
- **Những ai quan tâm đến Data Engineering** - stack Glue + Athena + S3 có thể áp dụng trực tiếp vào các vị trí data platform thực tế
- **Những người học tốt theo nhóm** - hình thức cộng tác làm cho trải nghiệm phong phú hơn nhiều so với tự học một mình

**Lý do?** Vì FCAJ lấp đầy khoảng cách giữa "tôi biết S3 là gì" và "tôi có thể thiết kế và triển khai một data lakehouse trên AWS." Khoảng cách đó chính xác là nơi hầu hết người tự học bị mắc kẹt. Chương trình cung cấp cấu trúc, môi trường AWS thực tế và cộng đồng để vượt qua nó.

Hình thức thực hành có nghĩa là bạn hoàn thành chương trình với thứ gì đó hữu hình: một pipeline đang hoạt động, code được tài liệu hóa, và sự tự tin để giải thích từng quyết định kiến trúc bạn đã đưa ra. Điều đó có giá trị hơn nhiều so với một chứng chỉ từ khóa học bạn xem ở tốc độ 1.5x.

---

## 5. Lời kết

Cảm ơn **đội ngũ FCJ** đã tạo ra và điều hành chương trình này. Công sức đầu tư vào thiết kế nội dung workshop, hỗ trợ người tham gia và xây dựng cộng đồng xung quanh việc học cloud thực sự rất rõ ràng.

Dành cho những người tham gia trong tương lai: **đừng sợ mắc lỗi.** Một số khoảnh khắc học hỏi quý giá nhất trong workshop này đến từ việc debug Glue job bị lỗi lúc nửa đêm hay tìm hiểu tại sao Streamlit dashboard từ chối kết nối. Những khoảnh khắc ma sát đó chính là nơi sự hiểu biết thực sự được xây dựng.

> *"Cách tốt nhất để học cloud architecture là làm hỏng thứ gì đó rồi sửa nó."* - Bài học FCAJ đã dạy tôi rất tốt.