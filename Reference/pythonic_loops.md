# Pythonic Loop Patterns Memo

## 1. Duyệt qua từng phần tử
```python
for x in arr:
    # xử lý x
```
- Dùng khi chỉ cần giá trị, không cần index.

## 2. Duyệt qua cả index và giá trị
```python
for i, x in enumerate(arr):
    # i là index, x là giá trị
```
- Dùng khi cần cả vị trí và giá trị.

## 3. Duyệt qua index (range)
```python
for i in range(len(arr)):
    # arr[i]
```
- Dùng khi cần truy cập nhiều phần tử theo index, hoặc cần so sánh arr[i] với arr[j].

## 4. Duyệt qua 2 mảng song song
```python
for a, b in zip(arr1, arr2):
    # xử lý a, b
```
- Dùng khi cần xử lý đồng thời 2 (hoặc nhiều) mảng cùng chiều dài.

## 5. Duyệt ngược
```python
for x in reversed(arr):
    # xử lý x từ cuối về đầu
```
- Dùng khi cần duyệt từ cuối về đầu.

## 6. Duyệt với điều kiện (list comprehension)
```python
[x for x in arr if x > 0]
```
- Dùng để tạo list mới theo điều kiện, rất Pythonic.

## 7. Duyệt qua dict
```python
for key, value in d.items():
    # xử lý key, value
```
- Dùng khi duyệt qua dict.

---
**Ghi nhớ:**
- Dùng `for x in arr` khi chỉ cần giá trị.
- Dùng `enumerate` khi cần cả index và giá trị.
- Dùng `range(len(arr))` khi cần truy cập index linh hoạt.
- Dùng `zip` khi cần duyệt song song nhiều mảng.
- Dùng list comprehension để tạo list mới nhanh, gọn.

Bạn có thể kết hợp các cách này để code Pythonic, ngắn gọn và dễ đọc hơn!
