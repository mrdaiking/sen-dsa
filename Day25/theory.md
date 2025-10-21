# Stack Theory – Day 25

## 1. Định nghĩa
- **Stack** là cấu trúc dữ liệu dạng LIFO (Last-In, First-Out).
- Phần tử được thêm vào cuối (top), và cũng được lấy ra từ cuối.

## 2. Các thao tác cơ bản
- **Push:** Thêm phần tử vào top.
- **Pop:** Lấy phần tử từ top ra.
- **Peek/Top:** Xem phần tử trên cùng mà không lấy ra.
- **isEmpty:** Kiểm tra stack có rỗng không.

## 3. Ứng dụng thực tế
- Kiểm tra dấu ngoặc hợp lệ (Valid Parentheses).
- Duyệt cây theo chiều sâu (DFS).
- Undo/Redo trong phần mềm.
- Biểu diễn call stack khi chạy hàm đệ quy.

## 4. Đặc điểm
- Truy cập chỉ được phần tử trên cùng.
- Thường dùng mảng (list) hoặc linked list để implement.

## 5. Python Stack
- Dùng list: `append()` để push, `pop()` để pop.
- Ví dụ:
```python
stack = []
stack.append(1)  # push
x = stack.pop()  # pop
stack[-1] # peek
```

## 6. Pattern nhận diện bài toán dùng Stack
- Cần kiểm tra thứ tự đóng/mở, lồng nhau (ngoặc, HTML tag).
- Cần lưu trạng thái tạm thời, quay lui (backtracking).
- Duyệt theo chiều sâu (DFS, toán học biểu thức).

## 7. Edge case khi dùng Stack
- Stack rỗng khi pop → cần kiểm tra trước khi pop.
- Tràn stack nếu push quá nhiều phần tử (thường gặp ở đệ quy sâu).

---

# Lời khuyên
- Stack là pattern cực kỳ phổ biến trong phỏng vấn DSA.
- Hiểu rõ thao tác push/pop và ứng dụng sẽ giúp bạn nhận diện bài toán nhanh hơn.
