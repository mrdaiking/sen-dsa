from typing import List

class Solution:
    """
    LeetCode 200: Number of Islands

    Given a 2D grid of '1's (land) and '0's (water), count the number of islands.
    An island is surrounded by water and formed by connecting adjacent lands
    horizontally or vertically.

    Approach: DFS traversal - when we find a '1', we explore the entire island
    by marking all connected '1's as visited ('0').
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r: int, c: int) -> None:
            """DFS to mark entire island as visited"""
            # Boundary and water checks
            if (
                r < 0 # Check if row index is out of bounds (top)
                or r >= rows # Check if row index is out of bounds (bottom)
                or c < 0 # Check if column index is out of bounds (left)
                or c >= cols # Check if column index is out of bounds (right)
                or grid[r][c] == '0' # Check if current cell is water or already visited
                ):
                return

            # Mark as visited
            grid[r][c] = '0'

            # Explore 4 directions
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right

        # Traverse the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)  # Mark entire island

        return islands


def test_number_of_islands():
    """Comprehensive test suite"""
    solution = Solution()

    # Test Case 1: Single island
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert solution.numIslands(grid1) == 1, "Test 1 failed"

    # Test Case 2: Multiple islands
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert solution.numIslands(grid2) == 3, "Test 2 failed"

    # Test Case 3: No islands
    grid3 = [
        ["0","0","0","0","0"],
        ["0","0","0","0","0"],
        ["0","0","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert solution.numIslands(grid3) == 0, "Test 3 failed"

    # Test Case 4: Single cell island
    grid4 = [["1"]]
    assert solution.numIslands(grid4) == 1, "Test 4 failed"

    # Test Case 5: Empty grid
    grid5 = []
    assert solution.numIslands(grid5) == 0, "Test 5 failed"

    # Test Case 6: All islands
    grid6 = [
        ["1","1","1"],
        ["1","1","1"],
        ["1","1","1"]
    ]
    assert solution.numIslands(grid6) == 1, "Test 6 failed"

    print("✅ All tests passed!")


if __name__ == "__main__":
    test_number_of_islands()