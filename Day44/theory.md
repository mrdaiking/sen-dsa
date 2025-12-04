# 🔢 **Day 44: Subarray Sum Equals K**

## 🎯 Problem Statement
Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals to `k`.

### Examples
**Example 1:**
```
Input: nums = [1,1,1], k = 2
Output: 2
Explanation: [1,1] at positions (0,1) and (1,2)
```

**Example 2:**
```
Input: nums = [1,2,3], k = 3
Output: 2
Explanation: [1,2] and [3]
```

### Constraints
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

## 🧠 Pattern Recognition
**Prefix Sum + HashMap Pattern:**
- Dùng prefix sum để tính tổng liên tục nhanh
- Dùng HashMap để lưu số lần xuất hiện của từng prefix sum

**Core Concept:**
- Với mỗi vị trí, nếu `prefix_sum - k` đã xuất hiện trước đó, nghĩa là có subarray kết thúc tại vị trí hiện tại có tổng bằng k

## 💡 Solution Approach
1. Khởi tạo prefix_sum = 0, hashmap lưu số lần xuất hiện của prefix_sum
2. Duyệt từng số trong nums:
   - Cộng vào prefix_sum
   - Nếu prefix_sum - k có trong hashmap → tăng count
   - Cập nhật hashmap với prefix_sum

## 📊 Complexity Analysis
- Time: O(n)
- Space: O(n)

## 🔍 Edge Cases
- nums có số âm
- k = 0
- nums toàn số 0
- subarray dài nhất, ngắn nhất

## 🎯 Interview Tips
- Prefix sum giúp tính tổng subarray nhanh
- HashMap giúp kiểm tra nhanh số lần xuất hiện
- Không cần duyệt mọi subarray (O(n^2)), chỉ cần O(n)

## 🔗 Pattern Connections
- Related: Longest Subarray Sum Equals K, Two Sum, Sliding Window

---
**Trước khi code, hãy thử nghĩ: Nếu bạn biết tổng từ đầu đến vị trí i, làm sao biết có subarray nào kết thúc ở i có tổng bằng k?**