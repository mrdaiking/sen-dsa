# Day 5: HashMap - Counting Problems

## Chủ đề
- Sử dụng HashMap (dictionary) để đếm tần suất phần tử/ký tự
- Nhận diện các bài toán cần so sánh tần suất (anagram, majority element, v.v.)

## Khi nào dùng pattern này?
- Khi cần kiểm tra số lần xuất hiện của phần tử/ký tự
- Khi cần so sánh hai tập hợp dựa trên tần suất

## Đặc điểm nhận diện
- Đề bài hỏi về "bao nhiêu lần xuất hiện"
- So sánh hai chuỗi/mảng về thành phần và số lượng

## Bài tập chính
- Valid Anagram (LeetCode 242)

## Template Python
```python
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
```

## Edge Cases
- Chuỗi rỗng
- Ký tự unicode
- Độ dài khác nhau

## Complexity
- Time: O(n)
- Space: O(1) (vì alphabet cố định, nếu không thì O(n))
