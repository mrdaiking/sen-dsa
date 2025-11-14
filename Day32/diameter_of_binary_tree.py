from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """Calculate the diameter of a binary tree using DFS recursion"""
        self.max_diameter = 0

        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            self.max_diameter = max(self.max_diameter, left + right)

            return 1 + max(left, right)
        
        dfs(root)

        return self.max_diameter

# ========================================
# COMPREHENSIVE TEST CASES
# ========================================
def test_diameter():
    solution = Solution()

    # Test Case 1: Example from problem
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)

    result1 = solution.diameterOfBinaryTree(root1)
    expected1 = 3  # Path: 4->2->5 or 4->2->1->3
    print(f"Test 1 - Balanced tree: {result1} (expected: {expected1}) - {'✅' if result1 == expected1 else '❌'}")

    # Test Case 2: Single node
    root2 = TreeNode(1)
    result2 = solution.diameterOfBinaryTree(root2)
    expected2 = 0
    print(f"Test 2 - Single node: {result2} (expected: {expected2}) - {'✅' if result2 == expected2 else '❌'}")

    # Test Case 3: Null tree
    result3 = solution.diameterOfBinaryTree(None)
    expected3 = 0
    print(f"Test 3 - Null tree: {result3} (expected: {expected3}) - {'✅' if result3 == expected3 else '❌'}")

    # Test Case 4: Skewed tree (all left)
    # 1
    #  \
    #   2
    #    \
    #     3
    root4 = TreeNode(1)
    root4.right = TreeNode(2)
    root4.right.right = TreeNode(3)
    result4 = solution.diameterOfBinaryTree(root4)
    expected4 = 2  # Path: 1->2->3
    print(f"Test 4 - Skewed tree: {result4} (expected: {expected4}) - {'✅' if result4 == expected4 else '❌'}")

    # Test Case 5: Perfect binary tree
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.right = TreeNode(3)
    root5.left.left = TreeNode(4)
    root5.left.right = TreeNode(5)
    root5.right.left = TreeNode(6)
    root5.right.right = TreeNode(7)
    result5 = solution.diameterOfBinaryTree(root5)
    expected5 = 4  # Path: 4->2->1->3->6 or similar
    print(f"Test 5 - Perfect tree: {result5} (expected: {expected5}) - {'✅' if result5 == expected5 else '❌'}")

if __name__ == "__main__":
    test_diameter()