# Day 18 - Sliding Window nâng cao: Longest Substring Without Repeating Characters

## 1. Khi nào dùng sliding window variable size?
- Khi cần tìm subarray/substring liên tiếp có thuộc tính động (ví dụ: không lặp ký tự, tổng không vượt quá k, v.v.)
- Khi window cần co giãn linh hoạt, không cố định độ dài

## 2. Đặc điểm nhận biết
- Input là chuỗi/mảng, yêu cầu subarray/substring liên tiếp dài nhất thỏa điều kiện
- Điều kiện có thể thay đổi trong quá trình duyệt (ví dụ: không lặp ký tự)

## 3. Tư duy giải quyết
- Dùng 2 con trỏ left, right để xác định window hiện tại
- Dùng HashSet/HashMap để kiểm soát các phần tử trong window
- Khi gặp phần tử trùng, di chuyển left để loại bỏ cho đến khi window hợp lệ
- Cập nhật kết quả tối ưu mỗi lần window hợp lệ
- Đảm bảo mỗi phần tử chỉ xét tối đa 2 lần → O(n)

## 4. Edge Cases
- Chuỗi rỗng
- Chuỗi toàn ký tự giống nhau
- Chuỗi rất dài
- Không có ký tự lặp

## 5. Template code
```python
s = "abcabcbb"
seen = set()
left = 0
max_len = 0
for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
    max_len = max(max_len, right - left + 1)
return max_len
```

---
Hãy trả lời các câu hỏi nhận diện pattern trước khi vào code nhé!