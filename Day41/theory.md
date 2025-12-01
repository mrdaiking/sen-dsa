# 🧩 **Day 41: Merge Intervals**

## 🎯 Problem Statement
Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

### Examples
**Example 1:**
```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: [1,3] and [2,6] overlap, merge to [1,6].
```

**Example 2:**
```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: [1,4] and [4,5] are considered overlapping.
```

### Constraints
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i <= end_i <= 10^4

## 🧠 Pattern Recognition
**Interval Pattern:** Sort intervals by start, then merge overlapping by comparing end points.

**Core Concept:**
- Sort intervals by start
- Duyệt từng interval, nếu chồng lên nhau thì gộp lại

## 💡 Solution Approach
1. **Sort intervals by start time**
2. **Duyệt từng interval:**
   - Nếu interval hiện tại không overlap với kết quả cuối cùng → thêm mới
   - Nếu overlap → cập nhật end lớn nhất

## 📊 Complexity Analysis
- Time: O(n log n) (do sort)
- Space: O(n) (output)

## 🔍 Edge Cases
- Intervals không overlap
- Intervals overlap hoàn toàn
- Intervals có cùng start hoặc end
- Một interval bao toàn bộ các interval khác

## 🎯 Interview Tips
- Luôn sort trước khi merge
- Chỉ cần duyệt một lần sau khi sort
- Đề bài merge interval xuất hiện rất nhiều trong thực tế (lịch, đặt phòng, v.v.)

## 🔗 Pattern Connections
- Next: Insert Interval, Meeting Rooms, Erase Overlap Intervals

---
**Trước khi code, hãy thử nghĩ: Nếu bạn có nhiều khoảng thời gian, làm sao biết hai khoảng có overlap?**