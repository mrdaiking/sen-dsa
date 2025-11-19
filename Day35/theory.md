# 🪜 **Day 35: Min Cost Climbing Stairs**

## 🎯 Problem Statement

You are given an integer array `cost` where `cost[i]` is the cost of `i-th` step on a staircase. Once you pay the cost, you can either climb one or two steps. You can either start from the step with index 0, or the step with index 1.

Return the **minimum cost** to reach the top of the floor.

### Examples

**Example 1:**
```
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
```

**Example 2:**
```
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
```

### Constraints

- `2 <= cost.length <= 1000`
- `0 <= cost[i] <= 999`

## 🧠 Pattern Recognition

**DP Pattern:** This is a **cost minimization** problem on a path with choices.

**State Definition:**
- `dp[i]` = **minimum cost** to reach step `i`
- Goal: `min(dp[n-1], dp[n-2])` (can reach top from either last or second-to-last step)

**Transition:**
```
dp[i] = cost[i] + min(dp[i-1], dp[i-2])
```

**Base Cases:**
- `dp[0] = cost[0]` (start at step 0)
- `dp[1] = cost[1]` (start at step 1)

## 💡 Solution Approaches

### 1. Bottom-Up DP (Tabulation)
- Use array to store minimum costs
- Time: O(n), Space: O(n)

### 2. Optimized DP (Space O(1))
- Only keep track of previous two minimums
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

- Minimum length: `[a, b]` → `min(a, b)`
- All zeros: `[0,0,0]` → 0
- Increasing costs: `[1,2,3,4]` → 1+3=4 (skip expensive steps)
- Alternating: `[1,100,1,100]` → 1+1=2

## 🎯 Interview Tips

- **Start from either step 0 or 1** - this is key!
- **Reach top from either n-1 or n-2** - don't forget this
- **Cost is paid when stepping on the stair**
- **Connect to House Robber:** Similar transition but minimize instead of maximize

## 🔗 Pattern Connections

- **Previous:** House Robber (maximize with constraints)
- **Next:** Coin Change (unbounded knapsack)
- **Related:** Climbing Stairs (count ways), Frog Jump

---

**How would you approach this problem? Think about the DP state and transition.**