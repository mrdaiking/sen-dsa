# 🏠 **Day 34: House Robber (Dynamic Programming)**

## 🎯 Problem Statement

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that **adjacent houses have security systems connected** and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return the **maximum amount of money you can rob tonight without alerting the police**.

### Examples

**Example 1:**
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

**Example 2:**
```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```

### Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

## 🧠 Pattern Recognition

**DP Pattern:** This is a classic **constraint-based DP** problem where you cannot take adjacent elements. Similar to:
- Climbing Stairs (unconstrained Fibonacci)
- But with the added constraint: **no two consecutive houses**

**State Definition:**
- `dp[i]` = maximum money you can rob from the first `i` houses
- Decision at each house: **rob it** (add `nums[i]` + `dp[i-2]`) or **skip it** (`dp[i-1]`)

**Transition:**
```
dp[i] = max(dp[i-1], nums[i] + dp[i-2])
```

**Base Cases:**
- `dp[0] = 0` (no houses)
- `dp[1] = nums[0]` (only first house)

## 💡 Solution Approaches

### 1. Bottom-Up DP (Tabulation)
- Use array to store results
- Time: O(n), Space: O(n)

### 2. Optimized DP (Space O(1))
- Only keep track of previous two values
- Time: O(n), Space: O(1)

### 3. Top-Down DP (Memoization)
- Recursive with memoization
- Time: O(n), Space: O(n)

## 📊 Complexity Analysis

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Bottom-Up | O(n) | O(n) | Straightforward |
| Optimized | O(n) | O(1) | Best for interviews |
| Memoization | O(n) | O(n) | Recursive elegance |

## 🔍 Edge Cases

- Empty array: `[]` → 0
- Single house: `[5]` → 5
- Two houses: `[1,2]` → max(1,2) = 2
- All zeros: `[0,0,0]` → 0
- Alternating high/low: `[1,100,1,100]` → 100 + 100 = 200

## 🎯 Interview Tips

- **Always consider the constraint first** - this changes everything from basic DP
- **Think about decisions**: At each step, choose between taking current + skip previous vs. taking previous
- **Space optimization** is key for large inputs
- **Connect to real problems**: Resource allocation, scheduling with conflicts

## 🔗 Pattern Connections

- **Previous:** Climbing Stairs (Fibonacci without constraints)
- **Next:** Min Cost Climbing Stairs (similar but with costs)
- **Related:** Jump Game, Subarray Sum problems

---

**How would you approach this problem? Think about the DP state and transition.**