# Day 14 - Search Insert Position (Binary Search)

## 1. Khi nào dùng Binary Search?
- Khi mảng đã sắp xếp (tăng/giảm dần)
- Khi cần tìm kiếm nhanh (O(log n))
- Khi đề bài hỏi về vị trí, sự tồn tại, hoặc thao tác insert/delete giữ thứ tự
****
## 2. Đặc điểm nhận biết bài Search Insert Position
- Input: mảng nums đã sort tăng dần, số target
- Output: index để chèn target vào sao cho mảng vẫn tăng dần
- Nếu target đã tồn tại, trả về index của nó
- Nếu không, trả về index nên chèn vào

## 3. Tư duy giải quyết
- Brute force: duyệt từng phần tử, O(n)
- Binary search: cắt đôi mảng, so sánh target với nums[mid]
    - Nếu target == nums[mid]: return mid
    - Nếu target < nums[mid]: tìm bên trái
    - Nếu target > nums[mid]: tìm bên phải
- Khi left > right, left chính là vị trí cần chèn target

## 4. Edge Cases
- target nhỏ hơn tất cả phần tử → return 0
- target lớn hơn tất cả phần tử → return len(nums)
- target nằm giữa hai phần tử → return index phần tử lớn hơn đầu tiên

## 5. Template code
```python
def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + **1**
        else:
            right = mid - 1
    return left
```

---
Hãy giải thích lại approach trước khi code nhé!