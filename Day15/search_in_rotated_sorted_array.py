"""
Day 15 - Search in Rotated Sorted Array
Leetcode: https://leetcode.com/problems/search-in-rotated-sorted-array/

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:
Input: nums = [1], target = 0
Output: -1

"""

def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]: # left side is sorted
           if nums[left] <= target < nums[mid]: # check if target is in the left side
                right = mid - 1
           else:
                left = mid + 1
        else: # right side is sorted
            if nums[mid] < target <= nums[right]: # check if target is in the right side
                left = mid + 1
            else:
                right = mid - 1
    return -1

# Test cases
if __name__ == "__main__":
    tests = [
        ([4,5,6,7,0,1,2], 0, 4),
        ([4,5,6,7,0,1,2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([1,3], 3, 1),
        ([5,1,3], 3, 2),
        ([1,2,3,4,5,6,7], 5, 4), # not rotated
    ]
    for nums, target, expected in tests:
        result = search(nums, target)
        print(f"Input: nums={nums}, target={target} | Output: {result} | Expected: {expected}")
