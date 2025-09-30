# Tổng kết phân tích Group Anagrams (Day 8)

- **Pattern:** HashMap grouping (key là đặc trưng của nhóm anagram)
- **Edge cases:** Chuỗi rỗng, chuỗi có một phần tử, chuỗi chứa số/ký tự đặc biệt/unicode (code vẫn xử lý được nhờ sorted)
- **Ý tưởng:**
    - Duyệt từng chuỗi, chuẩn hóa bằng sorted (tuple(sorted(s)))
    - Dùng key này để group vào HashMap (defaultdict(list))
    - Nếu key đã tồn tại thì append, chưa có thì tạo mới
    - Cuối cùng trả về list các values
- **Complexity:**
    - Time: O(N*KlogK) với N là số chuỗi, K là độ dài trung bình mỗi chuỗi (sort từng chuỗi)
    - Space: O(N*K) để lưu toàn bộ chuỗi vào HashMap
- **Pythonic improvements:**
    - Sử dụng defaultdict để tự động tạo list
    - sorted(s) hoạt động với mọi kiểu ký tự (số, đặc biệt, unicode)
    - List comprehension có thể dùng để xử lý kết quả
- **Ghi chú:**
    - Nếu dùng counting (tuple count ký tự) thay cho sort, có thể giảm xuống O(N*K) nhưng code phức tạp hơn
    - Độ phức tạp sort phụ thuộc vào thuật toán và dữ liệu thực tế

Bạn đã hoàn thành mock interview cho Group Anagrams!