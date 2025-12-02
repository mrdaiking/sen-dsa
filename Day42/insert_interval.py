from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i, n = 0, len(intervals)
        # add all intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i+=1
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1
        result.append(newInterval)

        while i < n:
            result.append(intervals[i])
            i+=1
        
        return result


def test_insert_interval():
    solution = Solution()
    # Test 1
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    assert solution.insert(intervals, newInterval) == [[1,5],[6,9]], "Test 1 failed"
    # Test 2
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    assert solution.insert(intervals, newInterval) == [[1,2],[3,10],[12,16]], "Test 2 failed"
    # Test 3: newInterval before all
    intervals = [[5,7],[8,10]]
    newInterval = [1,3]
    assert solution.insert(intervals, newInterval) == [[1,3],[5,7],[8,10]], "Test 3 failed"
    # Test 4: newInterval after all
    intervals = [[1,2],[3,4]]
    newInterval = [5,6]
    assert solution.insert(intervals, newInterval) == [[1,2],[3,4],[5,6]], "Test 4 failed"
    # Test 5: intervals empty
    intervals = []
    newInterval = [2,3]
    assert solution.insert(intervals, newInterval) == [[2,3]], "Test 5 failed"
    print("✅ All tests passed!")

if __name__ == "__main__":
    test_insert_interval()
