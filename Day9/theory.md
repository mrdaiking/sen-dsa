Tuyệt vời, mình sẽ tổng kết lại key insight buổi học Day 9 (Valid Palindrome - Two Pointers):

---

## 📊 Key Insight buổi hôm nay

1. **Pattern Two Pointers**  
   - Khi cần kiểm tra tính đối xứng, so sánh hai đầu dãy/chuỗi, two pointers là tối ưu nhất.
   - Hai con trỏ left, right di chuyển vào giữa, chỉ so sánh khi cả hai trỏ vào ký tự hợp lệ.

2. **Bỏ qua ký tự không hợp lệ**  
   - Có thể dùng regex để tiền xử lý chuỗi, hoặc dùng isalnum() để kiểm tra từng ký tự trực tiếp.
   - Dùng while lồng nhau để “nhích” con trỏ qua các ký tự không hợp lệ, nhưng tổng số bước vẫn chỉ O(n).

3. **So sánh không phân biệt hoa thường**  
   - Dùng .lower() để chuẩn hóa ký tự trước khi so sánh.

4. **Về vòng lặp và độ phức tạp**  
   - Dù có while lồng nhau, mỗi ký tự chỉ được kiểm tra tối đa một lần, nên tổng thể là O(n), không phải O(n²).
   - Trace tay từng bước giúp hiểu rõ bản chất vòng lặp và con trỏ.

5. **Edge case cần chú ý**  
   - Chuỗi rỗng, chỉ một ký tự, toàn ký tự đặc biệt, số, chữ hoa/thường.

6. **Tư duy học tập**  
   - Không ngại hỏi về những thứ cơ bản, càng hiểu sâu càng dễ master DSA.
   - Học tới đâu chắc tới đó, vướng đâu gỡ đó.

