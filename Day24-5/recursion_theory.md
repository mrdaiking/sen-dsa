# Recursion Mastery Session – Tổng kết lý thuyết

## 1. Định nghĩa
- Đệ quy (recursion) là kỹ thuật hàm tự gọi lại chính nó để giải quyết bài toán bằng cách chia nhỏ thành các bài toán con.

## 2. Cấu trúc hàm đệ quy
- **Điều kiện dừng (base case):** Tránh gọi vô hạn, thường là trạng thái nhỏ nhất hoặc cuối cùng.
- **Gọi lại chính nó với input nhỏ hơn:** Tạo công thức lặp (recurrence relation).
- **Xả stack:** Thao tác xử lý sau khi hàm con trả về.

## 3. Pattern nhận diện bài toán đệ quy
- Bài toán có thể chia nhỏ thành các bài toán con giống hệt bài toán gốc.
- Có công thức lặp rõ ràng (ví dụ: f(n) = f(n-1) + f(n-2)).
- Cấu trúc dữ liệu lồng nhau: cây, đồ thị, tổ hợp, backtracking.

## 4. Ví dụ kinh điển
- Factorial, Fibonacci
- Reverse Linked List (đệ quy)
- Tree Traversal (duyệt cây nhị phân)
- Sinh tổ hợp, hoán vị

## 5. Phân tích call stack
- Mỗi lần gọi hàm, một frame được đẩy vào stack.
- Khi gặp base case, stack bắt đầu xả ngược và trả kết quả lên trên.
- Có giá trị không đổi truyền ngược lên (ví dụ: new_head trong reverse linked list).

## 6. Ưu & nhược điểm
- **Ưu:** Code ngắn gọn, dễ hiểu cho bài toán phân rã tự nhiên.
- **Nhược:** Dễ tràn stack với input lớn, đôi khi chậm hơn vòng lặp.

## 7. Kinh nghiệm
- Luôn xác định rõ điều kiện dừng.
- Vẽ sơ đồ hoặc debug từng bước để kiểm tra trạng thái các biến/con trỏ.
- Nếu cần tối ưu bộ nhớ, cân nhắc chuyển sang vòng lặp hoặc tail recursion.

---

# Mẫu code reverse linked list (đệ quy)
```python
def reverse_linked_list_recursive(head):
    if not head or not head.next:
        return head
    new_head = reverse_linked_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
```

---

# Nhận diện đệ quy trong phỏng vấn
- Tìm công thức lặp hoặc mô hình phân rã bài toán.
- Đề bài có mô tả “giải quyết phần còn lại” hoặc “gọi lại chính nó”.
- Cấu trúc dữ liệu lồng nhau hoặc cần duyệt toàn bộ nhánh/cây.

---

# Lời khuyên
- Đệ quy là nền tảng cho tree, backtracking, dynamic programming.
- Hiểu bản chất xả stack và giá trị truyền ngược là chìa khóa để debug và tối ưu.
