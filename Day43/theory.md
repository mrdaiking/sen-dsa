# 🏃 **Day 43: Jump Game**

## 🎯 Problem Statement
You are given an integer array `nums`. You are initially positioned at the first index, and each element in the array represents your maximum jump length at that position.

Return `true` if you can reach the last index, or `false` otherwise.

### Examples
**Example 1:**
```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**
```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

### Constraints
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5

## 🧠 Pattern Recognition
**Greedy Pattern:** Track the farthest position we can reach, update as we go.

**Core Concept:**
- Duyệt từng vị trí, cập nhật vị trí xa nhất có thể đến được
- Nếu vị trí hiện tại > vị trí xa nhất → không thể tiếp tục
- Nếu vị trí xa nhất >= last index → có thể đến được

## 💡 Solution Approaches

### 1. Greedy (Recommended)
- Track max reachable position
- If current position > max reachable → return false
- If max reachable >= last index → return true
- Time: O(n), Space: O(1)

### 2. Dynamic Programming
- dp[i] = true if position i is reachable
- Time: O(n^2), Space: O(n)
- Not optimal for this problem

### 3. Backtracking
- Try all possible jumps (exponential)
- Time: O(2^n), not practical

## 📊 Complexity Analysis
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Greedy | O(n) | O(1) | Best approach |
| DP | O(n^2) | O(n) | Overkill |
| Backtracking | O(2^n) | O(n) | Too slow |

## 🔍 Edge Cases
- nums = [0] (already at last)
- nums = [0,1,2] (stuck at first)
- Large jumps that overshoot
- Multiple zeros in array

## 🎯 Interview Tips
- Greedy is optimal here
- Don't need to track actual path, just if reachable
- Update max_reach at each step
- Early termination when max_reach >= last index

## 🔗 Pattern Connections
- Related: Jump Game II (minimum jumps), Gas Station
- Greedy mindset: make locally optimal choice

---
**Trước khi code, hãy thử nghĩ: Nếu bạn đứng tại vị trí i, làm sao biết bạn có thể nhảy đến đó không?**