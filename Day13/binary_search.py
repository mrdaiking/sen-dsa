"""
Binary Search 
Leetcode Problem 704: https://leetcode.com/problems/binary-search/
Given a sorted array of integers and a target value, return the index of the target if found, otherwise return -1.
You may assume that all elements in the array are unique.
"""

def binary_search(nums, target):
    """
    Binary search algorithm to find the index of the target in the sorted array.
    Args:
        nums: List of integers.
        target: Integer.
    Returns:
        Integer: The index of the target if found, otherwise -1.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left +  right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 6, -1),
        ([], 1, -1),
        ([1], 1, 0),
        ([1, 3, 5, 7, 9], 7, 3),
    ]
    for idx, (nums, target, expected) in enumerate(test_cases, 1):
        result = binary_search(nums, target)
        print(f"Test case {idx}: {nums}, target={target}, expected={expected}")
        print(f"Result: {result}")
        print(f"Passed: {result == expected}")
        print("--------------------------------")
        
