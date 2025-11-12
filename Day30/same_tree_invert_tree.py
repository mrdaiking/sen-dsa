class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """Same Tree: Check if two trees are structurally identical with same values"""
        # Base cases: both None = True, one None = False
        if not p and not q:
            return True 
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        # Swap left, right
        root.left, root.right = root.right, root.left

        # Recurse on both subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root   # Return modified root

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # print("=== SAME TREE TESTS ===")

    # # Test 1: Both empty
    # print("Test 1 - Both empty:", solution.isSameTree(None, None))  # True

    # # Test 2: Same trees
    # p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    # q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    # print("Test 2 - Same trees:", solution.isSameTree(p1, q1))  # True

    # # Test 3: Different values
    # p2 = TreeNode(1, TreeNode(2), TreeNode(3))
    # q2 = TreeNode(1, TreeNode(2), TreeNode(4))
    # print("Test 3 - Different values:", solution.isSameTree(p2, q2))  # False

    # # Test 4: Different structure
    # p3 = TreeNode(1, TreeNode(2))
    # q3 = TreeNode(1, None, TreeNode(2))
    # print("Test 4 - Different structure:", solution.isSameTree(p3, q3))  # False

    print("\n=== INVERT TREE TESTS ===")

    # Test 5: Invert balanced tree
    root = TreeNode(4,
                    TreeNode(2, TreeNode(1), TreeNode(3)),
                    TreeNode(7, TreeNode(6), TreeNode(9)))

    print("Original tree structure:")
    print("       4")
    print("      / \\")
    print("     2   7")
    print("    / \\ / \\")
    print("   1  3 6  9")

    inverted = solution.invertTree(root)

    print("\nInverted tree structure:")
    print("       4")
    print("      / \\")
    print("     7   2")
    print("    / \\ / \\")
    print("   9  6 3  1")

    # Verify inversion by checking values
    print(f"\nVerification - Root: {inverted.val}")
    print(f"Root left: {inverted.left.val}, Root right: {inverted.right.val}")
    print(f"Root.left.left: {inverted.left.left.val}, Root.left.right: {inverted.left.right.val}")
    print(f"Root.right.left: {inverted.right.left.val}, Root.right.right: {inverted.right.right.val}")