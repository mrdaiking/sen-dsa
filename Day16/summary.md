# Day 16 - Binary Search Review (Tổng kết tuần 4)

## Key Points
- Binary Search dùng khi mảng đã sort hoặc có thể quy về sort (O(log n))
- Cốt lõi: mỗi lần cắt đôi, loại bỏ 1 nửa không thể chứa đáp án
- Template chung: left, right, mid; so sánh target với nums[mid] để điều chỉnh left/right
- Có thể áp dụng cho nhiều biến thể: tìm vị trí, insert, min/max, rotated array, tìm điều kiện thỏa mãn

## Edge Cases
- Mảng rỗng, chỉ 1 phần tử
- Target nhỏ hơn/lớn hơn tất cả phần tử
- Target trùng với nhiều phần tử (lower bound, upper bound)
- Mảng bị xoay (rotated), target ở đầu/cuối
- Mảng có số âm, số lớn, số trùng lặp

## Liên hệ với các pattern khác
- **Two Pointers:** Khi mảng đã sort, nhiều bài có thể giải bằng binary search hoặc two pointers (tìm cặp, subarray, v.v.)
- **Sliding Window:** Một số bài sliding window có thể kết hợp binary search trên answer (tìm min/max window)
- **Hashing:** Nếu mảng chưa sort, có thể dùng HashMap để tìm kiếm O(1), nhưng binary search tối ưu hơn khi đã sort
- **Binary Search on Answer:** Áp dụng cho các bài toán tìm min/max thỏa mãn điều kiện (ví dụ: tìm min capacity, min days, v.v.)
- **Recursion:** Binary search có thể viết dạng đệ quy, nhưng iterative thường tối ưu hơn về space

## Template tổng quát
```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

---
Bạn đã hoàn thành tuần Binary Search! Hãy luyện thêm các biến thể và kết hợp với các pattern khác để tăng phản xạ nhận diện nhé.
