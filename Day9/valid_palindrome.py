"""
Valid Palindrome - LeetCode 125 / NeetCode

Cho một chuỗi s, kiểm tra xem sau khi bỏ qua ký tự không phải chữ cái/chữ số và không phân biệt hoa thường, chuỗi đó có phải palindrome không?

Ví dụ:
Input: "A man, a plan, a canal: Panama"
Output: True

Input: "race a car"
Output: False

Input: " "
Output: True

Yêu cầu:
- Chỉ dùng O(1) bộ nhớ phụ
- Không dùng reverse string

"""

import re

def is_palindrome(s):
    """
    Kiểm tra chuỗi s có phải palindrome không (sau khi loại ký tự đặc biệt, không phân biệt hoa thường).
    Args:
        s: str
    Returns:
        bool

    Time: O(n)
    Space: O(n)
    """
    # Viết code ở đây
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()# Using regex to clean up the input and tranform to lower case
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome_v2(s):
    """
    Args:
        s: str
    Returns:
        bool

    Time: O(n)
    Space: O(1)
    """
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

# Test case
if __name__ == "__main__":
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
        "0P",
        "a",
        "ab@ba",
        "abcba",
        "abccba",
        "12321",
        "1231",
    ]
    # test_cases = ["madam"]
    for s in test_cases:
        print(f"Input: '{s}'")
        print(f"Output: {is_palindrome_v2(s)}\n")