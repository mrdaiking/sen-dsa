# Day 29: Maximum Depth Binary Tree

## 🎯 Problem Statement
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## 🧠 Approach
Use **recursion** with **post-order traversal**:
- Base case: if root is None, return 0
- Recursively calculate depth of left subtree
- Recursively calculate depth of right subtree
- Return 1 + max(left_depth, right_depth)

## 📊 Complexity Analysis
- **Time**: O(n) - visit each node once
- **Space**: O(h) - recursion stack depth equals tree height
  - Best case: O(log n) for balanced tree
  - Worst case: O(n) for skewed tree

## 🔑 Key Insights
- **Post-order traversal**: process left → right → current node
- **Recursion stack** depth = tree height
- **Base case** handles empty tree and leaf nodes
- **Max function** ensures we take the longer path

## 🔗 Pattern Connection
- Builds on **recursion fundamentals** from Day 24.5
- **Hierarchical recursion** vs linear recursion in linked lists
- First **tree traversal** pattern in Week 8

## 🎯 Next: Day 30 - Same Tree / Invert Tree
- More tree traversals and manipulations
- Practice recursive tree comparisons
