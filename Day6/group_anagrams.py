"""
Group Anagrams - NeetCode/LeetCode 49

Cho một mảng các chuỗi, hãy nhóm các chuỗi là anagram với nhau.

Ví dụ:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Giải thích: "eat", "tea", "ate" là anagram của nhau vì đều gồm các ký tự 'a', 'e', 't'.

Edge cases:
- Input: [""] → Output: [[""]]
- Input: ["a"] → Output: [["a"]]

Yêu cầu:
- Trả về danh sách các nhóm, thứ tự các nhóm không quan trọng.

"""
from collections import defaultdict

def group_anagrams(strs):
    """
    Nhóm các chuỗi là anagram với nhau.
    Args:
        strs: List[str] - mảng các chuỗi
    Returns:
        List[List[str]] - danh sách các nhóm anagram
    """
    # Viết code ở đây
    anagram_map = {}
    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s not in anagram_map:
            anagram_map[sorted_s] = []
                
    return list(anagram_map.values())

def group_anagrams_v2(strs):
    anagram_map = defaultdict(list) # Sử dụng defaultdict để tự động khởi tạo danh sách
    for s in strs:
        key = tuple(sorted(s)) # Sử dụng tuple vì list không thể làm key trong dict
        anagram_map[key].append(s)
    return list(anagram_map.values())

def is_anagram(s1, s2):

    if len(s1) != len(s2):
        return False
    count = {}
    for char in s1:
        count[char] = count.get(char, 0) + 1
    for char in s2:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
    for val in count.values():
        if val != 0:
            return False
    return True

# Test case
if __name__ == "__main__":
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"],
        ["abc", "bca", "cab", "bac", "acb", "cba"],
        ["abc", "def", "ghi"],
    ]
    for strs in test_cases:
        print(f"Input: {strs}")
        print(f"Output: {group_anagrams(strs)}\n")