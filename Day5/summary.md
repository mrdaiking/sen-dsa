# Day 5 Summary: Valid Anagram - Counting Pattern

## Key Insights
- Pattern: HashMap Counting (đếm tần suất ký tự/phần tử)
- Nhận diện: Khi đề yêu cầu so sánh số lần xuất hiện của phần tử giữa hai tập hợp (chuỗi/mảng)
- Cách giải: Dùng dict để đếm, so sánh dict hoặc giảm dần tần suất
- Pythonic: collections.Counter giúp code ngắn gọn, dễ đọc
- Edge cases: Chuỗi rỗng, ký tự unicode, độ dài khác nhau

## Pattern Template
```python
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in t:
        if c not in count or count[c] == 0:
            return False
        count[c] -= 1
    return True
```

## Connection to Previous Patterns
- Tiếp nối HashMap existence (Day 4), nhưng nhấn mạnh counting thay vì chỉ kiểm tra tồn tại
- Chuẩn bị cho các bài grouping phức tạp hơn (Day 6: Group Anagrams)

## Challenges
- Phân biệt rõ khi nào cần existence vs. counting
- Đảm bảo xử lý edge case (unicode, empty, unequal length)

---
Đã hoàn thành Day 5! Sẵn sàng cho Day 6: Group Anagrams.