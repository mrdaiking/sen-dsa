# 🌊 **Day 37: Number of Islands**

## 🎯 Problem Statement

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An **island** is surrounded by water and is formed by connecting adjacent lands **horizontally or vertically**. You may assume all four edges of the grid are all surrounded by water.

### Examples

**Example 1:**
```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

**Example 2:**
```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

### Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

## 🧠 Pattern Recognition

**Graph Pattern:** This is a **graph traversal** problem on a 2D grid.

**Core Concept:** Each land cell ('1') is a node, connected to adjacent land cells (up, down, left, right).

**Goal:** Count connected components in the grid graph.

**Key Insight:** When you find a '1', it's part of an island. Mark all connected '1's as visited to avoid double-counting.

## 💡 Solution Approaches

### 1. DFS (Depth-First Search)
- Traverse grid, when find '1', DFS to mark entire island as visited
- Time: O(m×n), Space: O(m×n) worst case

### 2. BFS (Breadth-First Search)
- Similar to DFS but use queue for level-order traversal
- Time: O(m×n), Space: O(min(m,n)) for queue

### 3. Union-Find (Disjoint Set Union)
- Treat each cell as a node, union adjacent '1's
- Time: O(m×n × α(m×n)), Space: O(m×n)

## 📊 Complexity Analysis

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| DFS | O(m×n) | O(m×n) | Recursive stack |
| BFS | O(m×n) | O(min(m,n)) | Iterative queue |
| Union-Find | O(m×n × α) | O(m×n) | Advanced, good for dynamic |

## 🔍 Edge Cases

- Empty grid: `[]` → 0
- No islands: All '0's → 0
- Single cell island: `[["1"]]` → 1
- All islands: All '1's → 1
- Islands at edges/corners

## 🎯 Interview Tips

- **Grid as Graph:** 4-directional connectivity (up, down, left, right)
- **Visited Marking:** Modify grid in-place or use separate visited set
- **Boundary Checks:** Always check grid boundaries before accessing
- **Connected Components:** Classic pattern for counting distinct groups

## 🔗 Pattern Connections

- **Previous:** Coin Change (DP on numbers)
- **Next:** Course Schedule (graph with cycles)
- **Related:** Surrounded Regions, Max Area of Island

---

**How would you approach this problem? Think about graph traversal on grid.**