# Day 7: Top K Frequent - HashMap + Sorting

## Khi nào gặp pattern này?
- Khi đề yêu cầu tìm K phần tử có tần suất xuất hiện cao nhất
- Khi cần ranking/xếp hạng dựa trên frequency
- Khi thấy từ khóa "Top K", "Most frequent", "K largest/smallest"

## Đặc điểm nhận diện
- Có yếu tố K trong đề bài
- Cần đếm tần suất + sắp xếp theo tần suất
- Thường trả về K phần tử, không phải toàn bộ

## Khác gì với các pattern trước?
- Day 4/5: HashMap dùng để count/existence
- Day 6: HashMap dùng để grouping
- Day 7: HashMap + Sorting/Priority Queue để tìm Top K

## Có thể kết hợp với pattern nào?
- Counting (HashMap để đếm tần suất)
- Sorting (sắp xếp theo frequency)
- Heap/Priority Queue (tối ưu cho Top K)

## Bài tập chính
- Top K Frequent Elements (LeetCode 347)

## Approaches có thể dùng:
1. HashMap + Sorting: O(N log N)
2. HashMap + Min Heap: O(N log K) 
3. HashMap + Bucket Sort: O(N) nhưng phức tạp

## Template Python (Sorting approach)
```python
from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    # Sort by frequency desc, return k elements
    return [x[0] for x in count.most_common(k)]
```

## Edge Cases
- K = 1, K = len(unique elements)
- Tần suất bằng nhau
- Mảng rỗng

## Complexity
- Time: O(N log N) với sorting, O(N log K) với heap
- Space: O(N) cho HashMap