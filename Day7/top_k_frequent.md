# Top K Frequent Elements (LeetCode 347)

## Đề bài
Cho một mảng số nguyên `nums` và một số nguyên `k`, hãy trả về `k` phần tử xuất hiện nhiều nhất.

Bạn có thể trả về kết quả theo bất kỳ thứ tự nào.

### Ví dụ:
```python
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
```

### Lưu ý:
- Đảm bảo rằng kết quả là duy nhất (không có case애매한)
- Có thể tối ưu độ phức tạp tốt hơn O(n log n)

### Ràng buộc:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k nằm trong khoảng [1, số lượng phần tử unique trong mảng]

## Yêu cầu
- Viết hàm `topKFrequent(nums: List[int], k: int) -> List[int]` để giải quyết bài toán này.
- Phân tích độ phức tạp thời gian và không gian.
- Thử implement cả approach sorting và heap (nếu có thời gian).