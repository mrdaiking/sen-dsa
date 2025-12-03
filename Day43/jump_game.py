from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        n = len(nums)
        for i in range(n):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= n - 1:
                return True
        return True


def test_jump_game():
    solution = Solution()
    # Test 1
    assert solution.canJump([2,3,1,1,4]) == True, "Test 1 failed"
    # Test 2
    assert solution.canJump([3,2,1,0,4]) == False, "Test 2 failed"
    # Test 3: Single element
    assert solution.canJump([0]) == True, "Test 3 failed"
    # Test 4: Stuck at first
    assert solution.canJump([0,1,2]) == False, "Test 4 failed"
    # Test 5: Large jump
    assert solution.canJump([5,0,0,0,0]) == True, "Test 5 failed"
    print("✅ All tests passed!")

if __name__ == "__main__":
    test_jump_game()
