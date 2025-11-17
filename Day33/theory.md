# Day 33: Climbing Stairs - DP Foundation

## 🎯 Problem Statement
You are climbing a staircase. It takes n steps to reach the top. Each time you can climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## 🧠 Key DP Concepts Introduced

### What is Dynamic Programming?
**DP** is a method for solving complex problems by breaking them down into simpler subproblems, solving each subproblem only once, and storing their solutions.

### Two Main Approaches:
1. **Bottom-up (Tabulation)**: Build solution from base cases up
2. **Top-down (Memoization)**: Recursive with caching

### When to Use DP?
- **Overlapping Subproblems**: Same subproblems solved multiple times
- **Optimal Substructure**: Solution built from optimal solutions of subproblems

## 💻 Algorithm Analysis

### State Definition
`dp[i]` = number of ways to reach step i

### Base Cases
- `dp[0]` = 1 (already at top)
- `dp[1]` = 1 (1 step)
- `dp[2]` = 2 (1+1 or 2)

### State Transition
`dp[i] = dp[i-1] + dp[i-2]`

**Why?** Last step is either 1 step (from i-1) or 2 steps (from i-2)

### Fibonacci Connection
The sequence: 1, 2, 3, 5, 8, 13, 21... is Fibonacci!

## 📊 Complexity Analysis

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Pure Recursion | O(2^n) | O(n) | Exponential - Bad! |
| Top-down DP | O(n) | O(n) | With memoization |
| Bottom-up DP | O(n) | O(n) | DP table |
| Optimized DP | O(n) | O(1) | Only 2 variables |

## 🔍 Why DP Works Here

### Overlapping Subproblems
```
climbStairs(5) calls:
├── climbStairs(4) and climbStairs(3)
├── climbStairs(4) calls climbStairs(3) and climbStairs(2)
├── climbStairs(3) calls climbStairs(2) and climbStairs(1)
└── climbStairs(2) is called 3 times! ❌
```

**DP solves this by computing each subproblem once and storing it.**

### Optimal Substructure
The optimal solution for n uses optimal solutions for n-1 and n-2.

## 💡 Implementation Patterns

### Bottom-up (Tabulation)
```python
def climbStairs(n):
    if n <= 2: return n

    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
```

### Top-down (Memoization)
```python
def climbStairs(n):
    memo = {}

    def dfs(steps):
        if steps in memo: return memo[steps]
        if steps <= 2: return steps

        memo[steps] = dfs(steps-1) + dfs(steps-2)
        return memo[steps]

    return dfs(n)
```

### Space Optimized
```python
def climbStairs(n):
    if n <= 2: return n

    prev2, prev1 = 1, 2
    for i in range(3, n+1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current

    return prev1
```

## 🎯 Interview Tips

- **Recognize Fibonacci pattern** in similar problems
- **Explain why DP is needed** (overlapping subproblems)
- **Show multiple approaches** (bottom-up vs top-down)
- **Mention space optimization** for Fibonacci-like problems
- **Consider edge cases**: n=0, n=1, n=2

## 🔗 Pattern Connections

- **Foundation for all DP problems**
- **Similar to**: House Robber, Min Cost Climbing Stairs, Coin Change
- **Real-world**: Path finding, sequence optimization, resource allocation

## 💭 Common Mistakes

1. **Wrong base cases**: n=0 should be 1, not 0
2. **Off-by-one errors**: dp array sizing
3. **Forgetting memoization**: Pure recursion is too slow
4. **Space waste**: Using O(n) when O(1) is possible

## 🚀 Next Steps
This pattern applies to:
- House Robber (Day 34)
- Min Cost Climbing Stairs (Day 35)
- Coin Change (Day 36)

*Master this transition and you master DP! 🧠*