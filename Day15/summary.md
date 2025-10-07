# Day 15 - Search in Rotated Sorted Array Tổng Kết

## Key Points
- Nhận diện pattern: mảng sort tăng dần nhưng bị xoay (rotated)
- Mỗi lần cắt đôi luôn có 1 nửa sorted, xác định bằng nums[left] <= nums[mid]
- So sánh target với đoạn sorted để quyết định loại bỏ nửa còn lại
- Độ phức tạp: O(log n) time, O(1) space
- Edge case: mảng không xoay, chỉ 1 phần tử, target không tồn tại, target ở đầu/cuối

## Template Code
```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

## Biến thể liên quan
- Tìm min/max trong mảng rotated (Find Minimum in Rotated Sorted Array)
- Tìm số lần xoay (pivot index)
- Tìm phần tử gần nhất, hoặc các bài binary search nâng cao khác

## Pythonic Tips
- Không cần sort lại mảng, không dùng extra space
- Có thể dùng recursion nhưng iterative sẽ tối ưu hơn về space

---
Bạn đã master Binary Search nâng cao cho mảng rotated! Hãy luyện thêm các biến thể để tăng phản xạ nhận diện pattern nhé.
