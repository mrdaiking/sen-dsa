"""
Max Area of Container
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Notice that you may not slant the container and n is at least 2.    
You may assume that n is at least 2.
Example 1:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:
Input: [1,1]
Output: 1
Explanation: The above vertical lines are represented by array [1,1]. In this case, the max area of water (blue section) the container can contain is 1.
Example 3:
Input: [4,3,2,1,4]
Output: 16
Explanation: The above vertical lines are represented by array [4,3,2,1,4]. In this case, the max area of water (blue section) the container can contain is 16.
Example 4:
Input: [1,2,1]
Output: 2
Explanation: The above vertical lines are represented by array [1,2,1]. In this case, the max area of water (blue section) the container can contain is 2.
Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""
from typing import List


def max_area(heights: List[int])-> int:
    """
    Find the maximum area of water that can be contained.
    
    Args:
        height: List[int] - list of non-negative integers representing heights of vertical lines.
    
    Returns:
        int - maximum area of water that can be contained.
    """

    left, right = 0, len(heights) - 1
    max_area = 0
    while left < right:
        area = min(heights[left], heights[right]) * (right - left)
        max_area = max(max_area, area)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area

if __name__ == "__main__":

    test_cases = [
        [1,8,6,2,5,4,8,3,7],
        [1,1],
        [4,3,2,1,4],
        [1,2,1],
        [1,3,2,5,25,24,5],
        [2,3,4,5,18,17,6],
        [1,2,4,3],
    ]

    expected = [
        49,
        1,
        16,
        2,
        24,
        17,
        4,
    ]
    for heights, exp in zip(test_cases, expected):
        print(f"Input: {heights}")
        print(f"Expected: {exp}\n")
        print(f"Output: {max_area(heights)}")
        if max_area(heights) != exp:
           print("FAIL\n")
        else:
           print("PASS\n")
