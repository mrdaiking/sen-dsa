"""
Day 44: Subarray Sum Equals K
Pattern: Prefix Sum + HashMap

Given an integer array nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example:
Input: nums = [1,1,1], k = 2
Output: 2

Approach:
- Use a hashmap to store the cumulative sum frequencies.
- For each element, compute the prefix sum.
- If (prefix_sum - k) exists in the hashmap, add its frequency to the result.
- Initialize hashmap with {0: 1} to handle subarrays starting at index 0.
"""
from typing import List

def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    count = 0
    prefix_sum = 0
    prefix_counts = {0: 1}
    for num in nums:
        prefix_sum += num
        count += prefix_counts.get(prefix_sum - k, 0)
        prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1
    return count

if __name__ == "__main__":
    # Minimal test
    print(subarray_sum_equals_k([1,1,1], 2))  # Output: 2
    # Edge case: negative numbers
    print(subarray_sum_equals_k([1,-1,0], 0))  # Output: 3
    # Large input
    print(subarray_sum_equals_k([0]*10000, 0))  # Output: 50005000
    # No subarray
    print(subarray_sum_equals_k([1,2,3], 7))  # Output: 0
