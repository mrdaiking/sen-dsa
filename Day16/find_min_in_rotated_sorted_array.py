"""
Day 16 - Find Minimum in Rotated Sorted Array
Leetcode: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Given the sorted rotated array nums of unique elements, return the minimum element of this array.
An array is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You must write an algorithm that runs in O(log n) time.
Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Example 3:
Input: nums = [11,13,15,17]
"""




def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

# Test cases
if __name__ == "__main__":
    tests = [
        ([3,4,5,1,2], 1),
        ([4,5,6,7,0,1,2], 0),
        ([11,13,15,17], 11),
        ([2,3,4,5,6,7,8,1], 1),
        ([1], 1),
        ([2,1], 1),
    ]
    for nums, expected in tests:
        result = findMin(nums)
        print(f"Input: nums={nums} | Output: {result} | Expected: {expected}")
