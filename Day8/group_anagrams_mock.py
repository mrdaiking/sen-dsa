# Day 8: Mini Mock Interview - Group Anagrams

from collections import defaultdict

def group_anagrams(strs):
    """
    Nhóm các chuỗi là anagram lại với nhau.
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))  # Key đặc trưng cho anagram
        groups[key].append(s)
    return list(groups.values())

# Test cases
if __name__ == "__main__":
    test_cases = [
        ["eat","tea","tan","ate","nat","bat"],
        [""],
        ["a"],
        ["abc","bca","cab","bac","acb","cba"],
        ["abc","def","ghi"],
        ["你好","好你","世界","界世"],
        [],
    ]
    for strs in test_cases:
        print(f"Input: {strs}")
        print(f"Output: {group_anagrams(strs)}\n")
