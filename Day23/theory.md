# Day 23 - Linked List Cycle (Floyd’s Tortoise and Hare)

## 1. Đề bài (Leetcode 141)
Cho head của một danh sách liên kết, kiểm tra xem danh sách có chu trình (cycle) hay không.

Ví dụ:
- Input: head = [3,2,0,-4], pos = 1 (node cuối trỏ về node thứ 2) → Output: True
- Input: head = [1,2], pos = 0 (node cuối trỏ về node đầu) → Output: True
- Input: head = [1], pos = -1 (không có chu trình) → Output: False

## 2. Pattern
- **Floyd’s Tortoise and Hare** (2 con trỏ chạy với tốc độ khác nhau):
    - slow: mỗi lần đi 1 bước
    - fast: mỗi lần đi 2 bước
    - Nếu có chu trình, fast sẽ bắt kịp slow tại một điểm nào đó.
- Nếu fast hoặc fast.next là None thì không có chu trình.

## 3. Các bước giải
1. Khởi tạo slow = head, fast = head
2. Lặp: slow = slow.next, fast = fast.next.next
3. Nếu slow == fast: có chu trình
4. Nếu fast hoặc fast.next là None: không có chu trình

## 4. Edge cases
- Danh sách rỗng (head = None)
- Danh sách chỉ có 1 node
- Chu trình ở node đầu hoặc cuối

## 5. Complexity
- Thời gian: O(n)
- Không gian: O(1)

---
