"""
LeetCode 242: Valid Anagram
Pattern: HashMap (Dictionary) for character counting
Link: https://leetcode.com/problems/valid-anagram/
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
Constraints:
- 1 <= s.length, t.length <= 5 * 104
- s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

from collections import defaultdict, Counter

def is_anagram(s: str, t: str) -> bool:
    """
    Returns True if t is an anagram of s, False otherwise.
    Approach: Count characters in both strings using HashMap and compare.
    Time: O(n)
    Space: O(1) (since alphabet size is fixed)
    """
    if len(s) != len(t):
        return False
    count = defaultdict(int)
    for char in s:
        count[char] += 1
    for char in t:
        count[char] -= 1
    for val in count.values():
        if val != 0:
            return False
    return True

def pythonic_is_anagram(s: str, t: str) -> bool:
    """
    Pythonic solution using collections.Counter.
    Returns True if t is an anagram of s, False otherwise.
    Time: O(n)
    Space: O(1) (if alphabet is fixed)
    """
    return Counter(s) == Counter(t)



# Example usage
if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))  # True
    print(is_anagram("rat", "car"))          # False
    print(is_anagram("你好世界", "界世好你"))    # True (unicode test)
    print(pythonic_is_anagram("anagram", "nagaram"))  # True
    print(pythonic_is_anagram("rat", "car"))          # False
    print(pythonic_is_anagram("你好世界", "界世好你"))    # True (unicode test)
