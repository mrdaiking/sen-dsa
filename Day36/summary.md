# 📊 **Day 36 Summary: Coin Change**

## 🎯 **Problem Solved**
**Coin Change** - Find minimum number of coins to make a given amount using unlimited supply of coin denominations.

## 🧠 **Key Learnings**

### ✅ **Pattern Recognition**
- **Sub-pattern:** "Unbounded Knapsack" - can use same item multiple times
- **Core Insight:** DP for minimum combinations with unlimited supply
- **State:** `dp[i]` = min coins to make amount i
- **Transition:** `dp[i] = min over coins of (dp[i - coin] + 1)`

### 💡 **Deep Understanding**
- **Unbounded Nature:** Unlike 0/1 knapsack, can reuse coins infinitely
- **Base Case:** `dp[0] = 0` (0 coins for amount 0)
- **Impossible Cases:** Return -1 when amount cannot be made
- **Optimization:** Same space O(amount) cannot be further reduced

### 🔧 **Technical Skills**
- **Bottom-up DP:** Implemented correctly with dp array
- **Edge Cases:** Amount 0, impossible amounts, single coin types
- **Performance:** O(coins × amount) time, suitable for typical constraints

## 🔗 **Pattern Connections**
- **Previous:** Min Cost Climbing Stairs (similar DP transition)
- **Next:** Word Break (unbounded pattern for strings)
- **Related:** Combination Sum (find all combinations)

## 📈 **Progress Update**
- **Confidence Level:** 5/5 (perfect implementation)
- **Time Spent:** ~45 minutes (thinking + implementation + testing)
- **Mistakes/Learnings:** Fixed incorrect test case ([3,7], 11 should be -1)

## 🎯 **Interview Readiness**
- **Time Complexity:** O(coins × amount)
- **Space Complexity:** O(amount)
- **Follow-up Questions:** Coin Change 2 (count ways), limited coin supply

---

**Next: Day 37 - Number of Islands** (Graph traversal)