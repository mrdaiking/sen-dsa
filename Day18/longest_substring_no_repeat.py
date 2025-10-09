"""
Day 18 - Longest Substring Without Repeating Characters (Sliding Window nâng cao)
Leetcode: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.  
"""

def lengthOfLongestSubstring(s):
    """
    Arguments:
    s : str : input string
    Returns:
    int : length of the longest substring without repeating characters
    """
    left = 0
    max_len = 0
    seen = set()
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

def lengthOfLongestSubstringv2(s):
    """
    Sliding window with dictionary to jump left pointer faster.
    """
    left = 0
    max_len = 0
    last_idx = {}
    for right, char in enumerate(s):
        if char in last_idx and last_idx[char] >= left:
            left = last_idx[char] + 1
        last_idx[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len



# Test cases
if __name__ == "__main__":
    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("a", 1),
        ("au", 2),
        ("dvdf", 3),
        ("abba", 2),
    ]
    for s, expected in tests:
        # result = lengthOfLongestSubstring(s)
        result = lengthOfLongestSubstringv2(s)

        assert result == expected, f"Fail: {s} -> {result} (expected {expected})"
        print(f"Input: s='{s}' | Output: {result} | Expected: {expected}")  
