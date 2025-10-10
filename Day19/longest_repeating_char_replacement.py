"""
Day 19 - Longest Repeating Character Replacement (Sliding Window biến thể)
Leetcode: https://leetcode.com/problems/longest-repeating-character-replacement/

Given a string s and an integer k, return the length of the longest substring containing the same letter you can get after performing at most k replacements.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Example 2:
Input: s = "AABABBA", k = 1
Output: 4

Constraints:
1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
"""

from itertools import count


def characterReplacement(s, k):
    """
    Slide window and count the frequent
    """
    left = 0
    max_len = 0
    count = {}
    max_count = 0

    for right, char in enumerate(s):
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
        max_count = max(max_count, count[char])
        if (right - left + 1 - max_count) > k:
            count[s[left]] -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len


# Test cases
if __name__ == "__main__":
    tests = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("AAAA", 2, 4),
        ("ABCDE", 1, 2),
        ("ABCDE", 0, 1),
        ("", 2, 0),
        ("A", 0, 1),
        ("A", 1, 1),
        ("ABBB", 2, 4),
        ("BAAAB", 2, 5),
    ]
    for s, k, expected in tests:
        result = characterReplacement(s, k)
        print(f"Input: s='{s}', k={k} | Output: {result} | Expected: {expected}")
