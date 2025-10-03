# Day 11 - 3Sum Tổng Kết

## Key Points
- 3Sum là bài toán kinh điển về tìm bộ ba số trong mảng sao cho tổng bằng 0, không trùng lặp.
- Sử dụng pattern: Sort + Two Pointers để tối ưu từ O(n³) xuống O(n²).
- Loại duplicate bằng cách skip các phần tử giống nhau ở cả 3 vị trí (i, left, right).
- Không loại duplicate trước khi xử lý, chỉ skip khi ghi nhận kết quả.
- Edge case: mảng rỗng, toàn số giống nhau, nhiều bộ ba trùng lặp, số âm/dương/0.

## Template Code Chuẩn
```python
def three_sum(nums):
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, n-1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return res
```

## Liên hệ các biến thể
- **3Sum Closest:** Tìm bộ ba có tổng gần nhất với target. Cách làm tương tự, chỉ cần lưu lại tổng gần nhất.
- **3Sum Smaller:** Đếm số bộ ba có tổng nhỏ hơn target. Dùng two pointers, mỗi lần tổng < target thì cộng thêm (right - left) vào kết quả.
- **4Sum, kSum:** Tổng quát hóa bằng cách fix 1 số, đệ quy hoặc lặp lại pattern two pointers cho k-2 số còn lại.
- **Two Pointers:** Áp dụng cho nhiều bài toán subarray, sliding window, tìm cặp số, v.v.

## Pythonic Tips
- Gán n = len(nums) đầu hàm để code gọn, tối ưu.
- Có thể dùng set để lưu kết quả unique nếu không muốn skip duplicate thủ công.
- Tận dụng sort để loại duplicate dễ dàng.

---
Bạn đã master pattern 3Sum! Hãy luyện thêm các biến thể để tăng phản xạ nhận diện pattern nhé.
