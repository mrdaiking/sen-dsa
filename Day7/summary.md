# Day 7 Summary: Top K Frequent Elements - HashMap + Sorting

## Key Insights
- Pattern: HashMap Counting + Sorting để tìm Top K
- Nhận diện: Khi đề yêu cầu "K phần tử có tần suất cao nhất", "Top K", "Most frequent"
- Approach chính: Count frequency → Sort → Slice top K

## Cách giải chi tiết
```python
def topKFrequent(nums, k):
    # 1. Đếm frequency bằng HashMap
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    # 2. Convert hashmap thành list of tuples và sort
    sorted_counts = sorted(count.items(), key=lambda x: x[1], reverse=True)
    
    # 3. Lấy K phần tử đầu tiên (chỉ lấy key, bỏ frequency)
    return [item[0] for item in sorted_counts[:k]]
```

## Memo quan trọng
- `count.items()` → list of tuples: `[(key, value), ...]`
- `sorted_counts[i][0]` = key của tuple thứ i
- `sorted_counts[i][1]` = frequency của tuple thứ i
- `[:k]` = slice K phần tử đầu tiên của list

## Các cách tối ưu khác
1. **Counter.most_common(k)** - Pythonic nhất:
   ```python
   from collections import Counter
   return [x[0] for x in Counter(nums).most_common(k)]
   ```

2. **Min Heap** - O(N log K) thay vì O(N log N):
   ```python
   import heapq
   # Dùng heap size K, chỉ giữ K phần tử có frequency cao nhất
   # Phức tạp nhưng tối ưu khi K << N
   ```

3. **Bucket Sort** - O(N) nhưng phức tạp:
   ```python
   # Tạo bucket theo frequency, duyệt ngược để lấy top K
   # Chỉ dùng khi cần optimize tối đa
   ```

## Connection to Previous Patterns
- Kế thừa HashMap counting (Day 4/5)
- Kết hợp với sorting để ranking
- Chuẩn bị cho các bài toán Heap/Priority Queue nâng cao

## Complexity
- Time: O(N log N) với sorting, O(N log K) với heap
- Space: O(N) cho HashMap

## Challenges
- Hiểu cách access list of tuples: `sorted_counts[i][0]`
- Nhận biết khi nào dùng Top K pattern
- Cân nhắc giữa đơn giản (sorting) và tối ưu (heap)

---
Đã hoàn thành Day 7! HashMap + Sorting pattern cho Top K problems.