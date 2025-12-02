# 🧩 **Day 42: Insert Interval**

## 🎯 Problem Statement
Given a list of non-overlapping intervals sorted by their start time, and a new interval, insert the new interval into the list (merge if necessary) so that the resulting list is still sorted and non-overlapping.

### Examples
**Example 1:**
```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

**Example 2:**
```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
```

### Constraints
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i <= end_i <= 10^4
- intervals is sorted and non-overlapping

## 🧠 Pattern Recognition
**Interval Pattern:** Duyệt qua các interval, xác định vị trí chèn, merge nếu cần.

**Core Concept:**
- Duyệt từng interval:
  - Nếu interval kết thúc trước newInterval bắt đầu → thêm vào kết quả
  - Nếu interval bắt đầu sau newInterval kết thúc → thêm newInterval, rồi thêm các interval còn lại
  - Nếu overlap → merge với newInterval

## 💡 Solution Approach
1. Duyệt từng interval, phân loại thành 3 trường hợp:
   - Trước newInterval
   - Sau newInterval
   - Overlap với newInterval
2. Merge các interval overlap với newInterval
3. Đảm bảo kết quả vẫn sort và không overlap

## 📊 Complexity Analysis
- Time: O(n)
- Space: O(n)

## 🔍 Edge Cases
- newInterval nằm ngoài tất cả các interval
- newInterval overlap với nhiều interval
- intervals rỗng
- newInterval không overlap với bất kỳ interval nào

## 🎯 Interview Tips
- Không cần sort lại vì intervals đã sort
- Merge giống như bài Merge Intervals nhưng chỉ với newInterval
- Dùng list để lưu kết quả, chèn đúng vị trí

## 🔗 Pattern Connections
- Previous: Merge Intervals
- Next: Meeting Rooms, Erase Overlap Intervals

---
**Trước khi code, hãy thử nghĩ: Nếu bạn có một khoảng mới, làm sao biết nó overlap với các khoảng cũ?**