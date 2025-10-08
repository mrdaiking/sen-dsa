# Day 17 - Sliding Window Tổng Kết

## Key Points
- Sliding Window dùng khi cần tìm subarray/substring liên tiếp tối ưu tổng, độ dài, hoặc thuộc tính nào đó.
- Có hai dạng chính:
  - Fixed size window: cửa sổ cố định, di chuyển left/right đều đặn.
  - Variable size window: cửa sổ thay đổi, left/right di chuyển linh hoạt theo điều kiện.
- Bài Best Time to Buy and Sell Stock là sliding window tối giản: chỉ cần lưu min_price và duyệt right, không cần left di chuyển độc lập.
- Độ phức tạp: O(n) time, O(1) space.

## Template Sliding Window
```python
# Fixed size window
for right in range(len(arr)):
    # add arr[right] vào window
    if window đủ size:
        # update kết quả
        # loại arr[left] khỏi window
        left += 1

# Variable size window
left = 0
for right in range(len(arr)):
    # add arr[right] vào window
    while window không hợp lệ:
        # loại arr[left] khỏi window
        left += 1
    # update kết quả nếu cần
```

## Edge Cases
- Mảng rỗng, 1 phần tử
- Tất cả phần tử giống nhau
- Không có subarray/substring thỏa mãn

## Liên hệ các pattern khác
- Dạng này là sliding window tối giản, chỉ cần lưu trạng thái tốt nhất (min_price) và một con trỏ duyệt.
- Các bài sliding window phức tạp hơn sẽ cần cả left/right di chuyển linh hoạt (ví dụ: longest substring without repeating, min window sum, v.v.)
- Có thể kết hợp với HashMap/Set để kiểm soát thuộc tính window (không lặp, đếm tần suất, v.v.)

---
Bạn đã master sliding window cơ bản! Hãy luyện thêm các biến thể variable window để tăng phản xạ nhận diện pattern nhé.
