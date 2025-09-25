# Day 5: Valid Anagram - Counting with HashMap

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in t:
        if c not in count or count[c] == 0:
            return False
        count[c] -= 1
    return True

# Pythonic version using collections.Counter
from collections import Counter

def is_anagram_counter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

# Test cases
if __name__ == "__main__":
    tests = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("a", "a", True),
        ("a", "b", False),
        ("ab", "a", False),
        ("你好", "好你", True),
    ]
    for s, t, expected in tests:
        assert is_anagram(s, t) == expected, f"Failed: {s}, {t}"
        assert is_anagram_counter(s, t) == expected, f"Counter Failed: {s}, {t}"
    print("All tests passed!")
