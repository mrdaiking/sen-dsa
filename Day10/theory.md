# Day 10: Two Sum II - Two Pointers trên mảng đã sắp xếp

## Khi nào gặp pattern này?
- Khi đề bài cho mảng đã sắp xếp (sorted array)
- Khi cần tìm cặp phần tử thỏa mãn điều kiện (tổng, hiệu, tích, v.v.)
- Khi có thể dùng hai đầu mảng để tối ưu

## Đặc điểm nhận diện
- Mảng đã sắp xếp
- Tìm cặp (pair) thỏa mãn điều kiện
- Có thể di chuyển left/right pointer để thu hẹp khoảng tìm kiếm

## Khác gì với Two Sum thường?
- Không cần HashMap, chỉ cần hai con trỏ
- Time: O(n), Space: O(1)

## Template Python
```python
def two_sum_ii(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]  # 1-based index
        elif s < target:
            left += 1
        else:
            right -= 1
```

## Edge Cases
- Không có cặp nào thỏa mãn
- Nhiều cặp thỏa mãn (trả về cặp đầu tiên)
- Số âm, số lớn, số nhỏ

## Complexity
- Time: O(n)
- Space: O(1)
