"""
Day 14 - Search Insert Position
Leetcode: https://leetcode.com/problems/search-insert-position/

Given a sorted array of integers nums and an integer target, return the index of the target if it is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:
Input: nums = [1], target = 0
Output: 0

Example 6:
Input: nums = [1], target = 2
Output: 1

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
"""

def searchInsert(nums, target):
    left, right = 0, len(nums) - 1

    while left<= right:
        mid = (left + right) // 2
        print(f"mid: {mid}, left: {left}, right: {right}")
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

    

# Test cases
if __name__ == "__main__":
    tests = [
        ([1,3,5,6], 5, 2),
        ([1,3,5,6], 2, 1),
        ([1,3,5,6], 7, 4),
        ([1,3,5,6], 0, 0),
        ([1, 3, 5, 6], 4, 2),
        ([1], 0, 0),
        ([1], 2, 1),
    ]
    for nums, target, expected in tests:
        result = searchInsert(nums, target)
        print(f"Input: nums={nums}, target={target} | Output: {result} | Expected: {expected}")
