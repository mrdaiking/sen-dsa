# Day 7: Top K Frequent Elements - HashMap + Sorting/Heap
"""
Example problem from LeetCode 347: https://leetcode.com/problems/top-k-frequent-elements/
Given a non-empty array of integers, return the k most frequent elements.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:
Input: nums = [1], k = 1
Output: [1]
Note: You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    sorted_counts = sorted(count.items(), key=lambda x: x[1], reverse=True)
    result = []
    for i in range(k):
        result.append(sorted_counts[i][0])  # [0] là key, [1] là frequency
    return result

if __name__ == "__main__":
    test_cases = [
        ([1,1,1,2,2,3], 2, [1,2]),
        ([1], 1, [1]),
        ([1,2], 2, [1,2]),
        ([1,1,1,2,2,3,3,3], 3, [1,2,3]),
        ([4,1,-1,2,-1,2,3], 2, [-1,2]),
        ([5,5,5,5], 1, [5])
    ]
    
    for i, (nums, k, expected) in enumerate(test_cases):
        result = topKFrequent(nums, k)
        print(f"Test case {i+1}: nums={nums}, k={k}, expected={expected}, got={result}")