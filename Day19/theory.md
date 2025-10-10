# Day 19 - Longest Repeating Character Replacement (Sliding Window biến thể)

## 1. Đề bài (Leetcode 424)
Cho chuỗi s chỉ gồm chữ cái in hoa và số nguyên k. Tìm độ dài substring dài nhất có thể nhận được bằng cách thay đổi tối đa k ký tự bất kỳ để tất cả ký tự trong substring đó giống nhau.

Ví dụ:
- Input: s = "ABAB", k = 2 → Output: 4 (thay 2 'A' thành 'B' hoặc ngược lại)
- Input: s = "AABABBA", k = 1 → Output: 4 (thay 1 'A' thành 'B' ở vị trí 4)

## 2. Pattern
- Sliding window biến thể: window vẫn di chuyển, nhưng cho phép tối đa k ký tự "khác biệt" trong window.
- Dùng dict (hoặc array 26) để đếm tần suất ký tự trong window.
- Quy tắc: Nếu (window size - max_freq) > k thì window không hợp lệ, cần thu nhỏ.

## 3. Các bước giải
1. Khởi tạo left, right, max_len, dict đếm tần suất.
2. Duyệt right, cập nhật count ký tự.
3. Nếu (window size - max_freq) > k: tăng left, giảm count.
4. Cập nhật max_len.

## 4. Edge case
- k = 0 (không được thay ký tự nào)
- Chuỗi toàn giống nhau
- Chuỗi toàn khác nhau
- k >= len(s)
- Chuỗi rỗng

## 5. Complexity
- Thời gian: O(n)
- Không gian: O(1) (vì chỉ có 26 ký tự)

---
