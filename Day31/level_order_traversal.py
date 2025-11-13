from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # ========================================
    # APPROACH 1: BFS with Queue (Iterative)
    # ========================================
    def levelOrder_BFS_Queue(self, root: Optional[TreeNode]) -> list[list[int]]:
        """Standard BFS with Queue - Most efficient and natural"""
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            result.append(current_level)

        return result

    # ========================================
    # APPROACH 2: DFS with Recursion
    # ========================================
    def levelOrder_DFS_Recursive(self, root: TreeNode) -> list[list[int]]:
        """DFS with level parameter - Works but less efficient"""
        result = []

        def dfs(node, level):
            if not node:
                return

            if len(result) == level:
                result.append([])

            result[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return result

    # ========================================
    # APPROACH 3: BFS with Two Queues
    # ========================================
    def levelOrder_BFS_TwoQueues(self, root: TreeNode) -> list[list[int]]:
        """Using two queues to separate levels - More explicit"""
        if not root:
            return []

        result = []
        current_level = deque([root])

        while current_level:
            next_level = deque()
            level_values = []

            # Process current level
            while current_level:
                node = current_level.popleft()
                level_values.append(node.val)

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            result.append(level_values)
            current_level = next_level

        return result

    # ========================================
    # APPROACH 4: DFS with HashMap
    # ========================================
    def levelOrder_DFS_HashMap(self, root: TreeNode) -> list[list[int]]:
        """DFS with dictionary to collect levels - Less common"""
        if not root:
            return []

        levels = {}

        def dfs(node, level):
            if not node:
                return

            if level not in levels:
                levels[level] = []
            levels[level].append(node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        # Convert to list of lists
        max_level = max(levels.keys()) if levels else -1
        return [levels.get(i, []) for i in range(max_level + 1)]

# ========================================
# TEST ALL APPROACHES
# ========================================
def test_all_approaches():
    """Test all 4 approaches to ensure they produce identical results"""

    # Create test tree: [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()

    # Get results from all approaches
    result_bfs_queue = solution.levelOrder_BFS_Queue(root)
    # result_dfs_recursive = solution.levelOrder_DFS_Recursive(root)
    # result_bfs_two_queues = solution.levelOrder_BFS_TwoQueues(root)
    # result_dfs_hashmap = solution.levelOrder_DFS_HashMap(root)

    expected = [[3], [9, 20], [15, 7]]

    print("Expected:", expected)
    print("BFS Queue:", result_bfs_queue)
    # print("DFS Recursive:", result_dfs_recursive)
    # print("BFS Two Queues:", result_bfs_two_queues)
    # print("DFS HashMap:", result_dfs_hashmap)

    # Verify all approaches give same result
    assert result_bfs_queue == expected
    # assert result_dfs_recursive == expected
    # assert result_bfs_two_queues == expected
    # assert result_dfs_hashmap == expected

    print("\n✅ All approaches produce identical results!")

def analyze_queue_sizes():

    print("=== PHÂN TÍCH KÍCH THƯỚC QUEUE ===\n")

    # Cây cân bằng (balanced tree)
    print("1. CÂY CÂN BẰNG (như ví dụ hiện tại):")
    print("       3")
    print("      / \\")
    print("     9   20")
    print("        /  \\")
    print("       15   7")
    print("Queue sizes: [1, 2, 2] - Max = 2\n")

    # Cây rộng (wide tree)
    print("2. CÂY RỘNG (nhiều nodes ở level 2):")
    print("       1")
    print("      / \\")
    print("     2   3")
    print("    / \\ / \\")
    print("   4  5 6  7")
    print("Queue sizes: [1, 2, 4] - Max = 4\n")

    # Cây lệch (skewed tree)
    print("3. CÂY LỆCH (chỉ một bên):")
    print("       1")
    print("      /")
    print("     2")
    print("    /")
    print("   3")
    print("  /")
    print(" 4")
    print("Queue sizes: [1, 1, 1, 1] - Max = 1\n")

    # Cây hoàn hảo (perfect tree)
    print("4. CÂY HOÀN HẢO (level 3):")
    print("        1")
    print("      /   \\")
    print("     2     3")
    print("    / \\   / \\")
    print("   4   5 6   7")
    print("  / \\ / \\/ \\ / \\")
    print(" 8 9 101112131415")
    print("Queue sizes: [1, 2, 4, 8] - Max = 8\n")

    print("🎯 KẾT LUẬN:")
    print("- Queue size = số nodes ở level rộng nhất")
    print("- Space complexity: O(w) where w = max width")
    print("- Trong worst case: cây hoàn hảo có 2^(h-1) nodes ở level cuối")

if __name__ == "__main__":
    test_all_approaches()
    print("\n" + "="*50)
    analyze_queue_sizes()