import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create adjacency list
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Initialize min-heap
        heap = [(0, k)]

        # Create dict save the shortest path
        dist = {}

        while heap:
            time, node = heapq.heappop(heap)
            if node in dist:
                continue # Already visited
            dist[node] = time

            for neighbor, w in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(heap, (time + w, neighbor))

        if len(dist) == n:
            return max(dist.values())
        return -1 


def test_network_delay_time():
    solution = Solution()
    # Test 1
    times = [[2,1,1],[2,3,1],[3,4,1]]
    assert solution.networkDelayTime(times, 4, 2) == 2, "Test 1 failed"
    # Test 2
    times = [[1,2,1]]
    assert solution.networkDelayTime(times, 2, 1) == 1, "Test 2 failed"
    # Test 3: Unreachable node
    times = [[1,2,1]]
    assert solution.networkDelayTime(times, 2, 2) == -1, "Test 3 failed"
    # Test 4: Multiple edges
    times = [[1,2,1],[1,2,2],[2,3,1]]
    assert solution.networkDelayTime(times, 3, 1) == 2, "Test 4 failed"
    # Test 5: Self-loop
    times = [[1,1,0],[1,2,1]]
    assert solution.networkDelayTime(times, 2, 1) == 1, "Test 5 failed"
    print("✅ All tests passed!")

if __name__ == "__main__":
    test_network_delay_time()
