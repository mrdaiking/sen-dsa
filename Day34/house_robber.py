from typing import List

class Solution:
    """
    House Robber - Maximize sum without robbing adjacent houses
    DP Pattern: Constraint-based optimization
    """

    def rob_bottom_up(self, nums: List[int]) -> int:
        """
        Bottom-Up DP with O(n) space
        dp[i] = max money from first i houses
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1]

    def rob_optimized(self, nums: List[int]) -> int:
        """
        Space-optimized DP: O(1) space
        Only track previous two maximums
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # prev2 = dp[i-2], prev1 = dp[i-1]
        prev2, prev1 = 0, 0

        for num in nums:
            # Current max: max(skip current, take current + prev2)
            current = max(prev1, num + prev2)
            # Update for next iteration
            prev2, prev1 = prev1, current

        return prev1

    def rob_memo(self, nums: List[int]) -> int:
        """
        Top-Down DP with memoization
        """
        memo = {}

        def dp(i: int) -> int:
            if i < 0:
                return 0
            if i in memo:
                return memo[i]

            # Don't rob current house
            skip = dp(i - 1)
            # Rob current house
            take = nums[i] + dp(i - 2)

            memo[i] = max(skip, take)
            return memo[i]

        return dp(len(nums) - 1)

    def rob_debug(self, nums: List[int]) -> int:
        """
        Debug version showing DP table building
        """
        if not nums:
            print("Empty array, return 0")
            return 0
        if len(nums) == 1:
            print(f"Single house: {nums[0]}")
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        print(f"Initial DP: {dp}")
        print(f"Base cases set: dp[0]={dp[0]}, dp[1]={dp[1]}")

        for i in range(2, len(nums)):
            skip_current = dp[i-1]
            take_current = nums[i] + dp[i-2]
            dp[i] = max(skip_current, take_current)
            print(f"i={i}: skip={skip_current}, take={nums[i]}+{dp[i-2]}={take_current}, dp[{i}]={dp[i]}")

        print(f"Final DP: {dp}")
        return dp[-1]


def test_house_robber():
    """Comprehensive test suite"""
    solution = Solution()

    # Test cases
    test_cases = [
        ([], 0, "Empty array"),
        ([5], 5, "Single house"),
        ([1, 2], 2, "Two houses"),
        ([1, 2, 3, 1], 4, "Example 1"),
        ([2, 7, 9, 3, 1], 12, "Example 2"),
        ([0, 0, 0], 0, "All zeros"),
        ([1, 100, 1, 100], 200, "Alternating"),
        ([100, 1, 1, 100], 200, "Max at ends"),
    ]

    print("🧪 Testing House Robber Solutions\n")

    for nums, expected, desc in test_cases:
        print(f"Test: {desc} - Input: {nums}")

        # Test all methods
        result_bottom = solution.rob_bottom_up(nums)
        # result_opt = solution.rob_optimized(nums)
        # result_memo = solution.rob_memo(nums)

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
    print("🔍 Debug Mode for [2, 7, 9, 3, 1]:")
    solution.rob_debug([2, 7, 9, 3, 1])
    print()

    # Performance comparison (for larger input)
    import time
    large_nums = list(range(1, 101))  # [1,2,3,...,100]

    print("⚡ Performance Comparison (n=100):")

    start = time.time()
    result1 = solution.rob_bottom_up(large_nums)
    time1 = time.time() - start

    # start = time.time()
    # result2 = solution.rob_optimized(large_nums)
    # time2 = time.time() - start

    # start = time.time()
    # result3 = solution.rob_memo(large_nums)
    # time3 = time.time() - start

    print(".4f")
    # print(".4f")
    # print(".4f")
    print(f"All results: {result1} (should be same)")


if __name__ == "__main__":
    test_house_robber()