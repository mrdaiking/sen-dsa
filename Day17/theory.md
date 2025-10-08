# Day 17 - Sliding Window Pattern Theory

## 1. Khi nào dùng Sliding Window?
- Khi cần tìm subarray/substring có tổng, độ dài, hoặc thuộc tính tối ưu trong mảng/chuỗi.
- Khi cần tối ưu từ O(n²) (dùng 2 vòng lặp) xuống O(n) bằng cách di chuyển cửa sổ liên tục.
- Khi chỉ cần xét các phần tử liên tiếp nhau (window liên tục).

## 2. Đặc điểm nhận biết
- Input là mảng/chuỗi, yêu cầu về subarray/substring liên tiếp.
- Tìm tổng lớn nhất/nhỏ nhất, độ dài lớn nhất/nhỏ nhất, substring không lặp, v.v.
- Có thể là window cố định (fixed size) hoặc thay đổi (variable size).

## 3. Tư duy giải quyết
- Dùng 2 con trỏ (left, right) để xác định window hiện tại.
- Di chuyển right để mở rộng window, left để thu hẹp khi cần.
- Cập nhật kết quả tối ưu mỗi lần window hợp lệ.
- Đảm bảo mỗi phần tử chỉ được xét tối đa 2 lần → O(n).

## 4. Edge Cases
- Mảng rỗng, chỉ 1 phần tử
- Tất cả phần tử giống nhau
- Window tràn ra ngoài mảng
- Không có subarray/substring thỏa mãn

## 5. Template code
```python
# Fixed size window
for right in range(len(arr)):
    # add arr[right] vào window
    if window đủ size:
        # update kết quả
        # loại arr[left] khỏi window
        left += 1

# Variable size window
left = 0
for right in range(len(arr)):
    # add arr[right] vào window
    while window không hợp lệ:
        # loại arr[left] khỏi window
        left += 1
    # update kết quả nếu cần
```

---
Hãy trả lời các câu hỏi nhận diện pattern trước khi vào code nhé!