# Day 30: Same Tree / Invert Tree

## 🎯 Problems

### 1. Same Tree
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

### 2. Invert Tree
Given the root of a binary tree, invert the tree, and return its root.

## 🧠 Approach

### Same Tree
Use **simultaneous recursion** on both trees:
- Base cases: both None → True, one None → False, values differ → False
- Recursive: same_tree(left_p, left_q) AND same_tree(right_p, right_q)

### Invert Tree
Use **post-order recursion**:
- Base case: if root is None, return None
- Recursively invert left and right subtrees
- Swap left and right children
- Return root

## 📊 Complexity Analysis
- **Time**: O(n) - visit each node once
- **Space**: O(h) - recursion stack depth

## 🔑 Key Insights
- **Same Tree**: Simultaneous traversal of two trees
- **Invert Tree**: Post-order with swap operation
- Both use recursive tree traversal patterns