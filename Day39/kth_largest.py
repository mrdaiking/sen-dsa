import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            print(f'min_heap: {min_heap}')
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
        


def test_kth_largest():
    solution = Solution()
    # Test 1
    assert solution.findKthLargest([3,2,1,5,6,4], 2) == 5, "Test 1 failed"
    # Test 2
    assert solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4, "Test 2 failed"
    # Test 3: k = 1 (max)
    assert solution.findKthLargest([1,2,3,4,5], 1) == 5, "Test 3 failed"
    # Test 4: k = len(nums) (min)
    assert solution.findKthLargest([1,2,3,4,5], 5) == 1, "Test 4 failed"
    # Test 5: Duplicates
    assert solution.findKthLargest([2,2,2,2,2], 3) == 2, "Test 5 failed"
    print("✅ All tests passed!")

if __name__ == "__main__":
    test_kth_largest()
