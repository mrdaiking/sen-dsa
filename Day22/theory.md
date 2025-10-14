# Day 22 - Merge Two Sorted Lists (Linked List Pattern)

## 1. Đề bài (Leetcode 21)
Cho hai danh sách liên kết đã được sắp xếp (sorted linked lists), hãy gộp chúng thành một danh sách liên kết đã sắp xếp mới.

Ví dụ:
- Input: list1 = [1,2,4], list2 = [1,3,4] → Output: [1,1,2,3,4,4]
- Input: list1 = [], list2 = [] → Output: []
- Input: list1 = [], list2 = [0] → Output: [0]

## 2. Pattern
- **Linked List Merge**: Dùng 2 con trỏ để duyệt qua 2 danh sách, so sánh và chọn node nhỏ hơn.
- **Dummy Node Technique**: Tạo node giả (dummy) để dễ dàng xây dựng danh sách kết quả.
- **Two Pointers**: Con trỏ chạy trên 2 danh sách khác nhau, không phải cùng một mảng.

## 3. Các bước giải
1. Tạo dummy node để bắt đầu danh sách kết quả.
2. Dùng 2 con trỏ để duyệt qua list1 và list2.
3. So sánh giá trị, chọn node nhỏ hơn, gắn vào kết quả.
4. Di chuyển con trỏ tương ứng.
5. Khi một danh sách hết, gắn phần còn lại của danh sách kia vào cuối.

## 4. Approaches
### Approach 1: Iterative (khuyến nghị)
- Dùng vòng lặp while, so sánh từng cặp node.
- Thời gian: O(m + n), không gian: O(1).

### Approach 2: Recursive
- Gọi đệ quy để so sánh và gộp.
- Thời gian: O(m + n), không gian: O(m + n) do call stack.

## 5. Edge cases
- Một hoặc cả hai danh sách rỗng.
- Danh sách có độ dài khác nhau nhiều.
- Tất cả phần tử của list1 < tất cả phần tử của list2 (hoặc ngược lại).
- Các phần tử trùng nhau.

## 6. Complexity
- Thời gian: O(m + n) với m, n là độ dài của 2 danh sách.
- Không gian: O(1) cho iterative, O(m + n) cho recursive.

## 7. Key insights
- Dummy node giúp code gọn gàng, tránh xử lý đặc biệt cho node đầu tiên.
- Sau khi một danh sách hết, có thể gắn trực tiếp phần còn lại của danh sách kia.
- Pattern này áp dụng được cho nhiều bài merge khác.

---