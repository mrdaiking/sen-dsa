# Day 12 - Mock Interview

## 🎯 Mock Interview Session
**Time: 20-25 phút | Focus: Mixed patterns (Arrays, Hashing, Two Pointers)**

---

## Problem 1: Container With Most Water (Medium)
**Time limit: 12-15 phút**

**Problem:**
Cho một mảng `height` với n đường thẳng đứng. Đường thẳng thứ i có hai điểm `(i, 0)` và `(i, height[i])`.

Tìm hai đường thẳng cùng với trục x tạo thành container chứa được nhiều nước nhất.

**Example:**
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: Các đường thẳng tại index 1 và 8 tạo container với area = min(8,7) * (8-1) = 49
```

**Constraints:**
- n >= 2
- 0 <= height[i] <= 10^4

---

**Hãy trả lời:**
1. **Pattern gì?** (2-3 phút suy nghĩ)
2. **Approach?** Giải thích cách tiếp cận trước khi code
3. **Time/Space complexity?**
4. **Edge cases?**

**Sau đó code solution:**

```python
def maxArea(height):
    # Your code here
    pass

# Test cases
test_cases = [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1,1], 1),
    ([4,3,2,1,4], 16),
    ([1,2,1], 2)
]
```

---

**⏰ Bắt đầu timer! Hãy giải thích approach trước khi code.**