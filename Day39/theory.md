# 🏆 **Day 39: Kth Largest Element in Array**

## 🎯 Problem Statement

Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array.

**Note:** It is the `k`th largest, not the `k`th distinct. (Duplicates count as separate elements.)

### Examples

**Example 1:**
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Explanation: The 2nd largest element is 5.
```

**Example 2:**
```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
Explanation: The 4th largest element is 4.
```

### Constraints
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

## 🧠 Pattern Recognition

**Heap Pattern:** This is a classic use-case for a **min-heap** (priority queue).

**Core Concept:**
- Maintain a heap of size k
- The top of the heap is the kth largest element

## 💡 Solution Approaches

### 1. Min-Heap (Priority Queue)
- Build a min-heap of size k
- For each number, push to heap; if heap size > k, pop smallest
- After all numbers, heap[0] is kth largest
- Time: O(n log k), Space: O(k)

### 2. Quickselect (Partition Algorithm)
- Like quicksort, but only partially sorts
- Average Time: O(n), Worst-case: O(n^2)
- Space: O(1)

### 3. Sorting
- Sort array descending, return nums[k-1]
- Time: O(n log n), Space: O(1) if in-place

## 📊 Complexity Analysis

| Approach    | Time      | Space   | Notes                |
|-------------|-----------|---------|----------------------|
| Min-Heap    | O(n log k)| O(k)    | Best for large n, small k |
| Quickselect | O(n) avg  | O(1)    | Fastest, but trickier |
| Sorting     | O(n log n)| O(1)    | Simple, not optimal   |

## 🔍 Edge Cases
- k = 1 (max element)
- k = len(nums) (min element)
- Duplicates
- Negative numbers
- Large arrays

## 🎯 Interview Tips
- Heap is best for streaming/online data
- Quickselect is fastest for static arrays
- Sorting is simplest, but not optimal for big data
- Know Python's `heapq` module

## 🔗 Pattern Connections
- Previous: Course Schedule (topological sort)
- Next: Network Delay Time (Dijkstra)
- Related: Kth Smallest, Top K Frequent, Median of Data Stream

---

**Trước khi code, hãy nghĩ: Nếu bạn phải tìm số lớn thứ k trong một mảng rất lớn, bạn sẽ dùng cách nào?**