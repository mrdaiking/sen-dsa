# Day 14 - Search Insert Position Tổng Kết

## Key Points
- Nhận diện pattern Binary Search khi mảng đã sort và cần tìm kiếm nhanh O(log n)
- Bài toán yêu cầu trả về index để chèn target vào mảng tăng dần
- Nếu target đã tồn tại, trả về index của nó
- Nếu không, trả về index nên chèn vào (left là vị trí cần chèn)
- Edge case: target nhỏ nhất, lớn nhất, nằm giữa, mảng 1 phần tử

## Template Code
```python
def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
```

## Biến thể liên quan
- Tìm phần tử đầu tiên lớn hơn hoặc bằng target (lower bound)
- Tìm phần tử cuối cùng nhỏ hơn hoặc bằng target (upper bound)
- Binary search trên answer (tìm min/max thỏa mãn điều kiện)
- Áp dụng cho các bài toán tìm kiếm vị trí, insert/delete giữ thứ tự

## Pythonic Tips
- Dùng bisect.bisect_left/right để giải nhanh các bài insert/search
- mid = left + (right - left) // 2 để tránh overflow (Python không bị nhưng là best practice)

---
Bạn đã master Binary Search cơ bản! Hãy luyện thêm các biến thể để tăng phản xạ nhận diện pattern nhé.
