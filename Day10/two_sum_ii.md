# Two Sum II (LeetCode 167)

## Đề bài
Cho một mảng số nguyên đã sắp xếp tăng dần `numbers` và một số nguyên `target`, hãy tìm chỉ số của hai số sao cho tổng của chúng bằng `target`.

Trả về chỉ số (1-based) của hai số đó dưới dạng một mảng `[index1, index2]` (index1 < index2).

Giả sử rằng mỗi input sẽ có đúng một đáp án và không dùng lại phần tử.

### Ví dụ:
```python
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

Input: numbers = [2,3,4], target = 6
Output: [1,3]

Input: numbers = [-1,0], target = -1
Output: [1,2]
```

### Ràng buộc:
- 2 <= len(numbers) <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers là mảng đã sắp xếp tăng dần
- Có đúng một đáp án

## Yêu cầu
- Viết hàm `two_sum_ii(numbers: List[int], target: int) -> List[int]`
- Phân tích độ phức tạp thời gian và không gian


---
## Tổng kết & Pythonic

- **Pattern:** Two Pointers trên mảng đã sắp xếp
- **Ý tưởng:**
    - Dùng hai con trỏ left/right, kiểm tra tổng
    - Nếu tổng nhỏ hơn target, tăng left; nếu lớn hơn, giảm right
    - Trả về index 1-based khi tìm thấy
- **Complexity:**
    - Time: O(n)
    - Space: O(1)
- **Pythonic improvements:**
    - Có thể viết ngắn hơn với:
    ```python
    def two_sum_ii(numbers, target):
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            left += (s < target)
            right -= (s > target)
    ```
    - Dùng enumerate cho test case:
    ```python
    for i, (numbers, target, expected) in enumerate(test_cases):
        result = two_sum_ii(numbers, target)
        print(f"Case {i+1}: {result} == {expected}")
    ```
- **Ghi chú:**
    - Không cần list comprehension vì chỉ cần trả về cặp đầu tiên
    - Code đã rất clean, không cần tối ưu thêm

---