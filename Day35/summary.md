# 📊 **Day 35 Summary: Min Cost Climbing Stairs**

## 🎯 **Problem Solved**
**Min Cost Climbing Stairs** - Minimize cost to reach top of staircase with 1 or 2 step jumps.

## 🧠 **Key Learnings**

### ✅ **Pattern Recognition**
- **Sub-pattern:** "Cost Minimization with Path Choices"
- **Core Insight:** DP for minimum cost paths with multiple options
- **State:** `dp[i]` = min cost to reach step i
- **Transition:** `dp[i] = cost[i] + min(dp[i-1], dp[i-2])`

### 💡 **Deep Understanding**
- **Start Options:** Can begin from step 0 or step 1
- **End Options:** Can reach top from either n-1 or n-2 step
- **Cost Payment:** Pay when stepping on the stair
- **Optimization:** Same space O(1) by tracking two previous costs

### 🔧 **Technical Skills**
- **Multiple Approaches:** Bottom-up, optimized, memoization
- **Debug Visualization:** Step-by-step cost accumulation
- **Edge Cases:** Empty, single, two steps, all zeros

## 🔗 **Pattern Connections**
- **Previous:** House Robber (maximize with constraints)
- **Next:** Coin Change (unbounded knapsack)
- **Related:** Climbing Stairs (count ways), Frog Jump

## 📈 **Progress Update**
- **Confidence Level:** 5/5 (deep understanding achieved)
- **Time Spent:** ~45 minutes (thinking + implementation + analysis)
- **Mistakes/Learnings:** Initially confused about start/end positions

## 🎯 **Interview Readiness**
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) optimized
- **Follow-up Questions:** Variable jump sizes, obstacles

---

**Next: Day 36 - Coin Change** (DP for minimum coins)