# Day 11 - 3Sum Pattern Theory

## 1. Khi nào dùng pattern 3Sum?
- Khi đề bài yêu cầu tìm bộ ba số (triplets) trong mảng thỏa mãn một điều kiện tổng (thường là tổng bằng 0 hoặc một giá trị cho trước).
- Thường gặp trong các bài toán: tìm tất cả bộ ba không trùng lặp, đếm số bộ ba, hoặc biến thể kSum.

## 2. Đặc điểm nhận biết
- Input: Một mảng số nguyên, có thể có số âm, dương, trùng lặp.
- Output: Danh sách các bộ ba (không trùng lặp) thỏa mãn điều kiện tổng.
- Ràng buộc: Không dùng brute-force O(n³), cần tối ưu hơn.

## 3. Tư duy giải quyết
- **Bước 1:** Sắp xếp mảng (sort) để dễ loại duplicate và dùng two pointers.
- **Bước 2:** Duyệt từng phần tử `i` (fix 1 số), dùng hai con trỏ `left`, `right` để tìm hai số còn lại sao cho tổng = target - nums[i].
- **Bước 3:** Loại bỏ duplicate bằng cách skip các số giống nhau ở cả 3 vị trí.
- **Độ phức tạp:** O(n²) (tốt nhất cho 3Sum).

## 4. Edge Cases
- Mảng rỗng hoặc ít hơn 3 phần tử.
- Tất cả số giống nhau.
- Có nhiều bộ ba trùng lặp.
- Số âm, số dương, số 0.

## 5. Biến thể liên quan
- 4Sum, kSum (tổng 4 số, k số)
- 3Sum Closest (tìm tổng gần nhất target)
- 3Sum Smaller (đếm bộ ba có tổng nhỏ hơn target)

## 6. Câu hỏi nhận diện pattern
- Khi nào dùng two pointers cho 3Sum?
- Làm sao loại duplicate hiệu quả?
- Tại sao phải sort trước?
- Có thể dùng HashSet không? Khi nào thì nên?

---
Hãy trả lời các câu hỏi trên trước khi vào code nhé!