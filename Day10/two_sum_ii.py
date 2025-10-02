# Day 10: Two Sum II - Two Pointers trên mảng đã sắp xếp
"""
Example problem from LeetCode 167: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Given a 1-indexed array of integers 'numbers' that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Return the indices of the two numbers (1-indexed) as an integer array answer of size 2,
where 1 <= answer[0] < answer[1] <= numbers.length.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.
Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Constraints:
2 <= numbers.length <= 3 * 10^4
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
Follow up: Could you implement a solution with O(n) time complexity and O(1) space complexity?
"""
from typing import List


def two_sum_ii(numbers: List[int], target: int) -> List[int]:
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    if not isinstance(numbers, list) or not numbers:
        raise ValueError("Input must be a non-empty list")
    
    if not isinstance(target, int):
        raise ValueError("Target must be an integer")
    if len(numbers) < 2:
        raise ValueError("The input array must contain at least two elements")
    left, right = 0, len(numbers) - 1
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left + 1, right + 1]
        elif sum < target:
            left += 1
        else:
            right -= 1
    return []

def two_sum_ii_pythonic(numbers: List[int], target: int) -> List[int]:
    """
    Pythonic approach using tuple unpacking and conditional expressions.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]
        left += (s < target)
        right -= (s > target)
    return []

if __name__ == "__main__":
    test_cases = [
        ([2,7,11,15], 9, [1,2]),
        ([2,3,4], 6, [1,3]),
        ([-1,0], -1, [1,2]),
        ([1,2,3,4,4,9,56,90], 8, [4,5]),
        ([1,3,4,5,7,10,11], 9, [3,4]),
    ]
    for numbers, target, expected in test_cases:
        result = two_sum_ii(numbers, target)
        print(f"Input: {numbers}, target={target}")
        print(f"Output: {result}, Expected: {expected}\n")
