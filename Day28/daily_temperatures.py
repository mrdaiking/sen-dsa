#!/usr/bin/env python3
"""
Day 28: Daily Temperatures
Pattern: Monotonic Stack (Next Greater Element)

Given an array of temperatures, return an array where answer[i] is the number of days
you have to wait after the ith day to get a warmer temperature. If there is no future day
for which this is possible, keep answer[i] == 0 instead.

Example:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Constraints:
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100
"""

def daily_temperatures(temperatures):
    """
    Time: O(n) - each element pushed/popped once
    Space: O(n) - stack can hold up to n elements
    """
    n = len(temperatures)
    answer = [0] * n
    stack = []  # store indices

    for i in range(n):  # iterate from right to left
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_day_idx = stack.pop()
            answer[prev_day_idx] = i - prev_day_idx
        stack.append(i)
    return answer


if __name__ == "__main__":
    # Test cases
    # Minimal
    assert daily_temperatures([73, 74]) == [1, 0]

    # Example
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]

    # Edge: all increasing
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]

    # Edge: all decreasing
    assert daily_temperatures([60, 50, 40, 30]) == [0, 0, 0, 0]

    # Edge: single element
    assert daily_temperatures([50]) == [0]

    # Large input (simulate)
    large_input = list(range(100000, 0, -1))  # decreasing
    result = daily_temperatures(large_input)
    assert result == [0] * 100000

    print("All tests passed! ✅")