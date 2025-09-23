"""
Two Sum Closest - LeetCode 16 variant

Given an array of integers and a target value, find the pair of numbers 
whose sum is closest to the target.

Return the sum of the two numbers (not the indices).

Example 1:
Input: nums = [1, 3, 4, 7, 10], target = 15
Output: 13  
Explanation: The pair (3, 10) gives sum 13, which is closest to 15

Example 2:
Input: nums = [-1, 2, 1, -4], target = 1
Output: 1
Explanation: The pair (-1, 2) gives sum 1, which exactly equals target 1

Example 3:
Input: nums = [1, 1, 1, 0], target = -100
Output: 1
Explanation: The pair (1, 0) gives sum 1, closest to target -100

Constraints:
- 2 <= nums.length <= 1000
- -1000 <= nums[i] <= 1000
- -1000 <= target <= 1000
"""

def two_sum_closest(nums, target):
    """
    Find the pair whose sum is closest to target.
    
    Args:
        nums: List of integers
        target: Target sum we want to get close to
    
    Returns:
        Integer: The sum closest to target
    """
    nums.sort()
    left, right = 0, len(nums) - 1
    closest_sum = 0
    min_distance = float('inf')

    while left < right:
        current_sum = nums[left] + nums[right]
        
        if abs(current_sum - target) < min_distance:
            min_distance = abs(current_sum - target)
            closest_sum = current_sum

        
        if current_sum < target:
            left += 1
        else:
            right -= 1

    return closest_sum


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 3, 4, 7, 10]
    target1 = 15
    result1 = two_sum_closest(nums1, target1)
    print(f"Input: {nums1}, target: {target1}")
    print(f"Output: {result1}")
    print()
    
    # Test case 2  
    nums2 = [-1, 2, 1, -4]
    target2 = 1
    result2 = two_sum_closest(nums2, target2)
    print(f"Input: {nums2}, target: {target2}")
    print(f"Output: {result2}")
    print()
    
    # Test case 3
    nums3 = [1, 1, 1, 0]
    target3 = -100
    result3 = two_sum_closest(nums3, target3)
    print(f"Input: {nums3}, target: {target3}")
    print(f"Output: {result3}")