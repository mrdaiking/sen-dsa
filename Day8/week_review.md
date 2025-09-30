# Day 8: Week 1-2 Review + Mini Mock Interview

## Mục tiêu
- Ôn lại toàn bộ pattern Arrays & Hashing (Days 1-7)
- Nhận diện nhanh pattern qua đề bài
- Thực hành mock interview: giải thích, code, phân tích complexity
- Tổng kết Pythonic syntax đã học

## Checklist review
- [ ] Two Sum (lookup)
- [ ] Valid Anagram (counting)
- [ ] Group Anagrams (grouping)
- [ ] Top K Frequent (sorting)
- [ ] Edge cases: empty, unicode, single element
- [ ] Pythonic: list comprehension, lambda, Counter, defaultdict

## Mini Mock Interview
### 1. Đề bài: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
- Pattern: Two Sum
- Yêu cầu: O(n) solution, giải thích tư duy

### 2. Đề bài: Given a list of strings, group anagrams together.
- Pattern: Group Anagrams
- Yêu cầu: Nhận diện key, giải thích grouping

### 3. Đề bài: Given a list of numbers, return the k most frequent elements.
- Pattern: Top K Frequent
- Yêu cầu: Phân tích sorting vs heap

## Pythonic Recap
- List comprehension: `[x for x in arr if x > 0]`
- Lambda: `sorted(arr, key=lambda x: x[1])`
- Counter: `Counter(arr).most_common(k)`
- Defaultdict: `groups = defaultdict(list)`

## Self-check
- Nhận diện pattern trong 2 phút?
- Giải thích rõ ràng?
- Code đúng, tối ưu?
- Biết cách viết Pythonic?

---
Bạn hãy tự ôn lại, chọn 1 đề mock interview để giải thích và code thử nhé!