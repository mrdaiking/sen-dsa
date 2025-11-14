# Day 32: Diameter of Binary Tree

## 🎯 Problem Statement
Given the root of a binary tree, return the length of the **diameter** of the tree.

The **diameter** of a binary tree is the **length of the longest path** between any two nodes in a tree. This path may or may not pass through the root.

The **length of a path** between two nodes is represented by the number of edges between them.

## 🧠 Key Insights

### What is Diameter?
- **Diameter**: Longest path between any two nodes
- **Path Length**: Number of edges (not nodes)
- **May or may not pass through root**

### Why DFS Recursion?
- Need to calculate height of each subtree
- Must track global maximum across all nodes
- Post-order traversal: process children before parent

### Three Cases Per Node
For each node, the diameter could be:
1. **Diameter of left subtree**
2. **Diameter of right subtree**
3. **Path through current node**: `height_left + height_right`

## 💻 Algorithm Walkthrough

### Example Tree:
```
       1
      / \
     2   3
    / \
   4   5
```

### DFS Traversal:
- **Node 4**: height = 1, diameter candidates = 0
- **Node 5**: height = 1, diameter candidates = 0
- **Node 2**: height = 2, diameter through node = 1+1=2
- **Node 3**: height = 1, diameter candidates = 0
- **Node 1**: height = 3, diameter through node = 2+1=3

**Final diameter: 3** (path: 4→2→1→3)

## 📊 Complexity Analysis

- **Time**: O(n) - Visit each node exactly once
- **Space**: O(h) - Recursion stack, h = tree height
  - Worst case: O(n) for skewed tree
  - Best case: O(log n) for balanced tree

## 🔍 Edge Cases

1. **Null tree**: diameter = 0
2. **Single node**: diameter = 0
3. **Two nodes**: diameter = 1
4. **Skewed tree**: diameter = n-1
5. **Balanced tree**: diameter varies

## 🔗 Pattern Connections

- **From Days 29-31**: Tree recursion patterns
- **Global tracking**: Similar to finding max in tree
- **Height calculation**: Foundation for many tree problems
- **Prepares for**: Tree DP, advanced tree algorithms

## 💡 Common Mistakes

1. **Forgetting global max**: Diameter may not pass through root
2. **Counting nodes instead of edges**: Path length = edges
3. **Not returning height**: Parent needs subtree height
4. **Wrong base case**: Null node height = 0

## 🎯 Interview Tips

- **Explain three cases** clearly
- **Draw example** on whiteboard
- **Mention complexity** confidently
- **Consider edge cases** in discussion