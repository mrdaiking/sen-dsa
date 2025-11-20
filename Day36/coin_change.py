from typing import List

class Solution:
    """
    Coin Change - Minimum coins to make amount
    DP Pattern: Unbounded Knapsack
    """

    def coinChange_bottom_up(self, coins: List[int], amount: int) -> int:
        """
        Bottom-Up DP with O(amount) space
        dp[i] = min coins to make amount i
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1

    def coinChange_optimized(self, coins: List[int], amount: int) -> int:
        """
        Space-optimized DP: O(amount) space (same as above, but cleaner)
        """
        # TODO: Implement optimized version
        pass

    def coinChange_memo(self, coins: List[int], amount: int) -> int:
        """
        Top-Down DP with memoization
        """
        # TODO: Implement memoization
        # Use a memo dict to store results
        # Recursive function: dp(amount) = min over coins of (1 + dp(amount - coin))
        pass

    def coinChange_debug(self, coins: List[int], amount: int) -> int:
        """
        Debug version showing DP table building
        """
        # TODO: Implement debug version
        # Show step-by-step DP table construction
        pass


def test_coin_change():
    """Comprehensive test suite"""
    solution = Solution()

    # Test cases: (coins, amount, expected, description)
    test_cases = [
        ([], 0, 0, "Empty coins, amount 0"),
        ([1], 0, 0, "Amount 0"),
        ([1, 2, 5], 11, 3, "Example 1: 5+5+1"),
        ([2], 3, -1, "Example 2: impossible"),
        ([1], 1, 1, "Single coin type"),
        ([1, 2], 4, 2, "Multiple ways: 2+2 or 1+1+1+1"),
        ([3, 7], 11, -1, "Impossible: 11 cannot be made from [3,7]"),
        ([1, 3, 4, 5], 7, 2, "4+3 or 5+2 or 1+1+5, etc."),
    ]

    print("🧪 Testing Coin Change Solutions\n")

    for coins, amount, expected, desc in test_cases:
        print(f"Test: {desc}")
        print(f"  Coins: {coins}, Amount: {amount}")

        # Test all methods (uncomment when implemented)
        result_bottom = solution.coinChange_bottom_up(coins, amount)
        # result_opt = solution.coinChange_optimized(coins, amount)
        # result_memo = solution.coinChange_memo(coins, amount)

        print(f"  Bottom-up: {result_bottom}")
        # print(f"  Optimized: {result_opt}")
        # print(f"  Memo: {result_memo}")
        print(f"  Expected: {expected}")

        # Verify all match (uncomment when implemented)
        assert result_bottom == expected, f"Bottom-up failed: {result_bottom} != {expected}"
        # assert result_opt == expected, f"Optimized failed: {result_opt} != {expected}"
        # assert result_memo == expected, f"Memo failed: {result_memo} != {expected}"

        print("  ✅ Test case noted\n")

    # Debug demonstration (uncomment when implemented)
    # print("🔍 Debug Mode for [1, 2, 5] and amount 11:")
    # solution.coinChange_debug([1, 2, 5], 11)
    # print()

    # Performance comparison (for larger input)
    # import time
    # large_coins = [1, 2, 5, 10, 20, 50, 100]
    # large_amount = 1000

    # print("⚡ Performance Comparison (amount=1000):")
    # start = time.time()
    # result1 = solution.coinChange_bottom_up(large_coins, large_amount)
    # time1 = time.time() - start
    # print(".4f")
    # print(f"Result: {result1}")


if __name__ == "__main__":
    test_coin_change()
