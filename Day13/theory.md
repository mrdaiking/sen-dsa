### 📊 Tổng kết Day 13 - Binary Search - Template Mastery

**1. Pattern:**  
- Binary Search (Tìm kiếm nhị phân)  
- Áp dụng khi mảng đã sắp xếp, cần tìm kiếm nhanh O(log n)

**2. Approach chuẩn:**  
- Khởi tạo left = 0, right = n-1  
- Lặp khi left <= right:  
    - Tính mid = (left + right) // 2  
    - Nếu nums[mid] == target: return mid  
    - Nếu nums[mid] < target: left = mid + 1  
    - Nếu nums[mid] > target: right = mid - 1  
- Nếu không tìm thấy: return -1

**3. Complexity:**  
- Thời gian: O(log n)  
- Bộ nhớ: O(1)

**4. Edge cases:**  
- Mảng rỗng  
- Target không tồn tại  
- Target ở đầu/cuối mảng  
- Mảng chỉ có 1 phần tử

**5. Pythonic:**  
- Không cần cắt mảng, chỉ thay đổi chỉ số  
- Sử dụng enumerate để test case rõ ràng  
- Code clean, dễ đọc

---

**Bạn đã hoàn thành xuất sắc Binary Search cơ bản!**  
- Đã hiểu sâu về pattern, template, edge case và cách test Pythonic.

---

#### ✅ Đã cập nhật tiến độ trong AGENTS.md  
**Tiếp theo:**  
- Day 14: Search Insert Position (Binary Search biến thể)
