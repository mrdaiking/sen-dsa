from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: # Handle input empty
            return []
        
        # Sort intervals by start
        intervals.sort(key=lambda x: x[0])
        print(f'INTERVALS: {intervals}')
        merged = [intervals[0]]
        print(f'MERGED: {merged}')
        # Merge intervals
        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)
        return merged


def test_merge_intervals():
    solution = Solution()
    # Test 1
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    assert solution.merge(intervals) == [[1,6],[8,10],[15,18]], "Test 1 failed"
    # Test 2
    intervals = [[1,4],[4,5]]
    assert solution.merge(intervals) == [[1,5]], "Test 2 failed"
    # Test 3: No overlap
    intervals = [[1,2],[3,4],[5,6]]
    assert solution.merge(intervals) == [[1,2],[3,4],[5,6]], "Test 3 failed"
    # Test 4: Full overlap
    intervals = [[1,10],[2,3],[4,8]]
    assert solution.merge(intervals) == [[1,10]], "Test 4 failed"
    # Test 5: Same start/end
    intervals = [[1,4],[1,4],[1,4]]
    assert solution.merge(intervals) == [[1,4]], "Test 5 failed"
    print("✅ All tests passed!")

if __name__ == "__main__":
    test_merge_intervals()
