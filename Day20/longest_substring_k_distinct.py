"""
Leetcode 340: Longest Substring with At Most K Distinct Characters
"""

def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    if k == 0 or not s:
        return 0
    left = 0
    max_len = 0
    count = {}
    for right, char in enumerate(s):
        count[char] = count.get(char, 0) + 1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len


def test_length_of_longest_substring_k_distinct():
    # Edge cases
    assert length_of_longest_substring_k_distinct("", 2) == 0
    assert length_of_longest_substring_k_distinct("aaaa", 1) == 4
    assert length_of_longest_substring_k_distinct("aabbcc", 0) == 0
    assert length_of_longest_substring_k_distinct("aabbcc", 10) == 6
    # Normal cases
    assert length_of_longest_substring_k_distinct("eceba", 2) == 3  # "ece"
    assert length_of_longest_substring_k_distinct("aa", 1) == 2
    assert length_of_longest_substring_k_distinct("abcadcacacaca", 3) == 11  # "acacacacaca""cadcacacaca"
    print("All test cases passed!")

if __name__ == "__main__":
    test_length_of_longest_substring_k_distinct()

# --- Tóm tắt bài Leetcode 340 ---
# Pattern: Sliding Window biến thiên + HashMap
# Khi nào dùng: Tìm chuỗi con dài nhất thỏa mãn số lượng ký tự khác nhau ≤ K
# Template:
#   - Dùng dict để đếm số lần xuất hiện ký tự trong window
#   - Mở rộng right, nếu số ký tự khác nhau > K thì co left
#   - Luôn cập nhật max_len
# Edge case: chuỗi rỗng, K = 0, K lớn hơn số ký tự khác nhau
# Pythonic:
#   - count[char] = count.get(char, 0) + 1 để rút gọn cập nhật dict
#   - Có thể dùng collections.Counter hoặc defaultdict(int) nếu muốn code ngắn hơn
