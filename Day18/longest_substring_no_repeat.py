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
        print(f"right: {right}, s[right]: {s[right]}, seen: {seen}")
        while s[right] in seen:
            print(f'remove {s[left]}')
            seen.remove(s[left])
            left += 1
            print(f"left: {left}, seen: {seen}")
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

def lengthOfLongestSubstring_set(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        print(f"\n--- right={right}, char='{s[right]}' ---")
        print(f"Before: char_set={char_set}, left={left}")
        while s[right] in char_set:
            print(f"  Duplicate '{s[right]}', remove '{s[left]}' at left={left}")
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        print(f"After: char_set={char_set}, left={left}")
        print(f"Window: '{s[left:right+1]}', length={right - left + 1}")
        max_length = max(max_length, right - left + 1)
        print(f"  New max_length: {max_length}")
    return max_length




# Test cases
if __name__ == "__main__":
    tests = [
        ("abcabcbb", 3)
        # ("bbbbb", 1),
        # ("pwwkew", 3),
        # ("", 0),
        # ("a", 1),
        # ("au", 2),
        # ("dvdf", 3),
        # ("abba", 2),
    ]
    for s, expected in tests:
        # result = lengthOfLongestSubstring(s)
        result = lengthOfLongestSubstring(s)
        print(f'-----------------------------')
        lengthOfLongestSubstring_set(s)

        # assert result == expected, f"Fail: {s} -> {result} (expected {expected})"
        # print(f"Input: s='{s}' | Output: {result} | Expected: {expected}")  
