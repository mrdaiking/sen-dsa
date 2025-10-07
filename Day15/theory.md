# Day 15 - Search in Rotated Sorted Array (Binary Search nâng cao)

## 1. Khi nào dùng pattern này?
- Khi mảng đã sort tăng dần nhưng bị xoay (rotated) tại một điểm bất kỳ.
- Đề bài yêu cầu tìm kiếm phần tử (target) trong mảng này với O(log n).

## 2. Đặc điểm nhận biết
- Mảng không còn hoàn toàn tăng dần, nhưng mỗi lần cắt đôi (binary search) luôn có ít nhất 1 nửa là sorted.
- Phải xác định nửa nào sorted để quyết định loại bỏ nửa còn lại.

## 3. Tư duy giải quyết
- Dùng binary search bình thường: left, right, mid
- Nếu nums[mid] == target: return mid
- Xác định nửa nào sorted:
    - Nếu nums[left] <= nums[mid]: nửa trái sorted
    - Nếu nums[mid] <= nums[right]: nửa phải sorted
- So sánh target với đoạn sorted để quyết định di chuyển left/right
- Lặp lại cho đến khi tìm thấy hoặc left > right

## 4. Edge Cases
- Mảng không xoay (sorted bình thường)
- Mảng chỉ có 1 phần tử
- Target không tồn tại
- Target ở đầu/cuối mảng

## 5. Template code
```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # Nửa trái sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Nửa phải sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

---
Hãy trả lời các câu hỏi nhận diện pattern trước khi vào code nhé!