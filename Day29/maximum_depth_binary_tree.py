class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Empty tree
    print("Test 1 - Empty tree:", solution.maxDepth(None))  # Expected: 0

    # Test case 2: Single node
    root1 = TreeNode(1)
    print("Test 2 - Single node:", solution.maxDepth(root1))  # Expected: 1

    # Test case 3: Balanced tree
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    root2 = TreeNode(3)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(7)
    print("Test 3 - Balanced tree:", solution.maxDepth(root2))  # Expected: 3
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(7)
    print("Test 3 - Balanced tree:", solution.maxDepth(root2))  # Expected: 3