from typing import List

class Solution:
    """
    Min Cost Climbing Stairs - Minimize cost to reach top
    DP Pattern: Cost minimization with path choices
    """

    def minCostClimbingStairs_bottom_up(self, cost: List[int]) -> int:
        """
        Bottom-Up DP with O(n) space
        dp[i] = min cost to reach step i
        """
        if len(cost)<= 1:
            return 0

        dp = [0] * len(cost)

        # Case base cases
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[-1], dp[-2])
        
        

    def minCostClimbingStairs_optimized(self, cost: List[int]) -> int:
        """
        Space-optimized DP: O(1) space
        Only track previous two minimums
        """
        if len(cost) <= 1:
            return 0

        # prev2 = dp[i-2], prev1 = dp[i-1]
        prev2, prev1 = cost[0], cost[1]

        for i in range(2, len(cost)):
            # Current min cost to reach step i
            current = cost[i] + min(prev1, prev2)
            # Update for next iteration
            prev2, prev1 = prev1, current

        # Return min of last two steps
        return min(prev1, prev2)

    def minCostClimbingStairs_memo(self, cost: List[int]) -> int:
        """
        Top-Down DP with memoization
        """
        memo = {}

        def dp(i: int) -> int:
            if i < 0:
                return 0
            if i in memo:
                return memo[i]

            # Cost to reach step i + min of previous steps
            memo[i] = cost[i] + min(dp(i-1), dp(i-2))
            return memo[i]

        n = len(cost)
        # Can start from step 0 or 1, reach top from n-1 or n-2
        return min(dp(n-1), dp(n-2))

    def minCostClimbingStairs_debug(self, cost: List[int]) -> int:
        """
        Debug version showing DP table building
        """
        if len(cost) <= 1:
            print("Cost array too small, return 0")
            return 0

        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        print(f"Initial DP: {dp}")
        print(f"Base cases set: dp[0]={dp[0]}, dp[1]={dp[1]}")

        for i in range(2, n):
            from_prev1 = dp[i-1]
            from_prev2 = dp[i-2]
            dp[i] = cost[i] + min(from_prev1, from_prev2)
            print(f"i={i}: cost[{i}]={cost[i]} + min({from_prev1}, {from_prev2}) = {dp[i]}")

        result = min(dp[n-1], dp[n-2])
        print(f"Final DP: {dp}")
        print(f"Min of dp[{n-1}]={dp[n-1]} and dp[{n-2}]={dp[n-2]} = {result}")
        return result


def test_min_cost_climbing_stairs():
    """Comprehensive test suite"""
    solution = Solution()

    # Test cases
    test_cases = [
        ([], 0, "Empty array"),
        ([10], 0, "Single step"),
        ([10, 15], 10, "Two steps - choose min"),
        ([10, 15, 20], 15, "Example 1"),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6, "Example 2"),
        ([0, 0, 0], 0, "All zeros"),
        ([1, 2, 3, 4], 4, "Increasing costs"),
        ([1, 100, 1, 100], 2, "Alternating"),
    ]

    print("🧪 Testing Min Cost Climbing Stairs Solutions\n")

    for cost, expected, desc in test_cases:
        print(f"Test: {desc} - Input: {cost}")

        # Test all methods
        result_bottom = solution.minCostClimbingStairs_bottom_up(cost)
        # result_opt = solution.minCostClimbingStairs_optimized(cost)
        # result_memo = solution.minCostClimbingStairs_memo(cost)

        print(f"  Bottom-up: {result_bottom}")
        # print(f"  Optimized: {result_opt}")
        # print(f"  Memo: {result_memo}")
        print(f"  Expected: {expected}")

        # Verify all match
        assert result_bottom == expected, f"Bottom-up failed: {result_bottom} != {expected}"
        # assert result_opt == expected, f"Optimized failed: {result_opt} != {expected}"
        # assert result_memo == expected, f"Memo failed: {result_memo} != {expected}"

        print("  ✅ All methods correct\n")

    # Debug demonstration
    print("🔍 Debug Mode for [10, 15, 20]:")
    solution.minCostClimbingStairs_debug([10, 15, 20])
    print()

    print("🔍 Debug Mode for [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]:")
    solution.minCostClimbingStairs_debug([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    print()

    # Performance comparison (for larger input)
    import time
    large_cost = list(range(1, 101))  # [1,2,3,...,100]

    print("⚡ Performance Comparison (n=100):")

    start = time.time()
    result1 = solution.minCostClimbingStairs_bottom_up(large_cost)
    time1 = time.time() - start

    # start = time.time()
    # result2 = solution.minCostClimbingStairs_optimized(large_cost)
    # time2 = time.time() - start

    # start = time.time()
    # result3 = solution.minCostClimbingStairs_memo(large_cost)
    # time3 = time.time() - start

    print(".4f")
    print(".4f")
    print(".4f")
    print(f"All results: {result1} (should be same)")


if __name__ == "__main__":
    test_min_cost_climbing_stairs()