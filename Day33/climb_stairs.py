

class Solution:
    # ========================================
    # APPROACH 1: Bottom-up DP (Tabulation)
    # ========================================
    def climbStairs_DP_BottomUp(self, n: int) -> int:
        """Standard DP approach using array - O(n) time, O(n) space"""
        if n <= 2:
            return n # No need to return for 1,2

        dp = [0] * (n + 1) # Create dynamic programming array

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    # ========================================
    # APPROACH 1B: Bottom-up DP (Debug Version)
    # ========================================
    def climbStairs_DP_BottomUp_Debug(self, n: int) -> int:
        """Debug version showing step-by-step DP table building"""
        print(f"\n=== DEBUG: climbStairs_DP_BottomUp(n={n}) ===")

        if n <= 2:
            print(f"Base case: n <= 2, return {n}")
            return n

        # DP table: dp[i] = ways to reach step i
        dp = [0] * (n + 1)
        print(f"Initial DP array: {dp}")

        dp[1] = 1  # 1 way to reach step 1
        dp[2] = 2  # 2 ways to reach step 2
        print(f"After setting base cases: {dp}")

        # Fill DP table
        print("\nFilling DP table:")
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            print(f"  i={i}: dp[{i}] = dp[{i-1}] + dp[{i-2}] = {dp[i-1]} + {dp[i-2]} = {dp[i]}")
            print(f"       Current DP: {dp}")

        result = dp[n]
        print(f"\nFinal result: dp[{n}] = {result}")
        print("=" * 50)

        return result

    # ========================================
    # APPROACH 2: Top-down DP (Memoization)
    # ========================================
    # def climbStairs_DP_TopDown(self, n: int) -> int:
    #     """Recursion with memoization - O(n) time, O(n) space"""
    #     memo = {}

    #     def dfs(steps):
    #         if steps in memo:
    #             return memo[steps]

    #         if steps <= 2:
    #             return steps

    #         memo[steps] = dfs(steps - 1) + dfs(steps - 2)
    #         return memo[steps]

    #     return dfs(n)

    # ========================================
    # APPROACH 3: Optimized DP (Constant Space)
    # ========================================
    # def climbStairs_DP_Optimized(self, n: int) -> int:
    #     """Space optimized - O(n) time, O(1) space"""
    #     if n <= 2:
    #         return n

    #     # Only track last two values
    #     prev2 = 1  # ways to reach step 1
    #     prev1 = 2  # ways to reach step 2

    #     for i in range(3, n + 1):
    #         current = prev1 + prev2
    #         prev2 = prev1
    #         prev1 = current

    #     return prev1

    # ========================================
    # APPROACH 4: Pure Recursion (Inefficient)
    # ========================================
    # def climbStairs_Recursion(self, n: int) -> int:
    #     """Pure recursion - O(2^n) time, O(n) space - For comparison only"""
    #     if n <= 2:
    #         return n
    #     return self.climbStairs_Recursion(n - 1) + self.climbStairs_Recursion(n - 2)

# ========================================
# COMPREHENSIVE TEST CASES
# ========================================
def test_all_approaches():
    """Test all approaches with various inputs"""

    solution = Solution()

    # Test cases: (n, expected_result)
    test_cases = [
        (0, 0),  # Edge case
        (1, 1),  # Base case
        (2, 2),  # Base case
        (3, 3),  # First DP step
        (4, 5),  # Fibonacci pattern
        (5, 8),  # Fibonacci pattern
        (6, 13), # Fibonacci pattern
        (10, 89), # Larger input
    ]

    approaches = [
        ("Bottom-up DP", solution.climbStairs_DP_BottomUp),
        # ("Top-down DP", solution.climbStairs_DP_TopDown),
        # ("Optimized DP", solution.climbStairs_DP_Optimized),
    ]

    print("=== TESTING ALL DP APPROACHES ===\n")

    for n, expected in test_cases:
        print(f"Testing n = {n} (expected: {expected})")

        results = []
        for name, func in approaches:
            try:
                result = func(n)
                status = "✅" if result == expected else "❌"
                results.append(f"{name}: {result} {status}")
            except Exception as e:
                results.append(f"{name}: ERROR - {e}")

        for result in results:
            print(f"  {result}")

        # Check if all approaches agree
        approach_results = [func(n) for _, func in approaches]
        if len(set(approach_results)) == 1:
            print("  🎯 All approaches agree!")
        else:
            print("  ⚠️  Approaches disagree!")

        print()

    # Performance comparison for larger n
    print("=== PERFORMANCE COMPARISON ===")
    import time

    n = 35  # Large enough to see difference

    for name, func in approaches:
        start_time = time.time()
        result = func(n)
        end_time = time.time()

        elapsed = (end_time - start_time) * 1000  # milliseconds
        print(".2f")

if __name__ == "__main__":
    test_all_approaches()

    # Debug demonstration
    print("\n" + "="*60)
    print("DEBUG DEMONSTRATION - Step by step DP building")
    print("="*60)

    solution = Solution()

    # Test with small n to see step-by-step
    test_cases = [3, 4, 5]

    for n in test_cases:
        result = solution.climbStairs_DP_BottomUp_Debug(n)
        print(f"✅ Result for n={n}: {result}\n")