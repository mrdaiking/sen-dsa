# Day 12 - Two Pointers Pattern Review

## Week 3 Recap: Two Pointers Mastery

### Patterns đã học (Days 9-11):

#### **Day 9: Valid Palindrome - Basic Two Pointers**
- **Pattern:** Kiểm tra chuỗi palindrome từ hai đầu vào giữa
- **Approach:** left = 0, right = n-1, so sánh chars, bỏ qua non-alphanumeric
- **Time/Space:** O(n), O(1)
- **Key insight:** Two pointers đơn giản nhất, dễ nhận biết

#### **Day 10: Two Sum II - Sorted Array**
- **Pattern:** Tìm cặp số trong mảng đã sort có tổng = target
- **Approach:** left = 0, right = n-1, tăng left nếu sum < target, giảm right nếu sum > target
- **Time/Space:** O(n), O(1) - tối ưu hơn HashMap O(n) space
- **Key insight:** Lợi dụng mảng sorted để di chuyển pointers hiệu quả

#### **Day 11: 3Sum - Fix + Two Pointers**
- **Pattern:** Tìm bộ ba số có tổng = 0, không trùng lặp
- **Approach:** Sort + fix một số i, dùng two pointers cho hai số còn lại
- **Time/Space:** O(n²), O(1) - tối ưu từ O(n³) brute force
- **Key insight:** Kết hợp sort, fix element, two pointers, skip duplicates

---

## Pattern Recognition Questions

**Trả lời các câu hỏi sau để test hiểu biết:**

### 1. Khi nào dùng Two Pointers?
- Input là mảng/chuỗi đã sort hoặc có thể sort được?
- Cần tìm cặp/bộ số thỏa mãn điều kiện tổng?
- Cần kiểm tra palindrome, symmetric properties?
- Muốn optimize space từ O(n) xuống O(1)?

### 2. Các dạng Two Pointers chính:
- **Opposite direction:** left/right từ hai đầu (palindrome, pair sum)
- **Same direction:** slow/fast pointers (linked list, sliding window)
- **Fix + Two Pointers:** kSum problems (3Sum, 4Sum)

### 3. Template chung:
```python
# Opposite direction
left, right = 0, len(arr) - 1
while left < right:
    if condition_met:
        # process result
        left += 1
        right -= 1
    elif need_increase:
        left += 1
    else:
        right -= 1
```

### 4. Pitfalls thường gặp:
- Quên skip duplicates trong kSum
- Không kiểm tra bounds (left < right)
- Sai logic di chuyển pointers

---

## Quick Quiz - Pattern Recognition

**Xem đề bài, nói ngay pattern nào:**

1. "Tìm cặp số trong sorted array có tổng gần nhất k"
2. "Kiểm tra string có phải palindrome không"  
3. "Tìm tất cả bộ ba số có tổng bằng target"
4. "Container with most water"
5. "Remove duplicates from sorted array in-place"

---

**Sẵn sàng trả lời các câu hỏi chưa? Sau đó sẽ chuyển sang mock interview!**