from typing import List

class Solution:
    """
    LeetCode 207: Course Schedule
    Determine if you can finish all courses given prerequisites.
    Approach: DFS cycle detection (3-state)
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Visualize the input as adjacency list
        adj = [[] for _ in range(numCourses)] # Define the size of array as same as the course size
        for dest, src in prerequisites:
            adj[src].append(dest)

        # 0: unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses

        def dfs(node: int) -> bool:
            if state[node] == 1:
                return False # Found cycle
            if state[node] == 2:
                return True # Already processed, no cycle here
            state[node] = 1 # Mark as visited
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            state[node] = 2 # Mark as visited
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
       


def test_course_schedule():
    solution = Solution()
    # Test 1: No cycle
    assert solution.canFinish(2, [[1,0]]) == True, "Test 1 failed"
    # Test 2: Simple cycle
    assert solution.canFinish(2, [[1,0],[0,1]]) == False, "Test 2 failed"
    # Test 3: Multiple courses, no cycle
    assert solution.canFinish(4, [[1,0],[2,0],[3,1],[3,2]]) == True, "Test 3 failed"
    # Test 4: Self-loop
    assert solution.canFinish(1, [[0,0]]) == False, "Test 4 failed"
    # Test 5: Disconnected graph
    assert solution.canFinish(3, [[1,0]]) == True, "Test 5 failed"
    # Test 6: Empty prerequisites
    assert solution.canFinish(3, []) == True, "Test 6 failed"
    print("✅ All tests passed!")

if __name__ == "__main__":
    test_course_schedule()
