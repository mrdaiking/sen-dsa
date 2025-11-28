# ⏱️ **Day 40: Network Delay Time (Dijkstra)**

## 🎯 Problem Statement

You are given a network of `n` nodes, labeled `1` to `n`. You are given a list `times`, where `times[i] = [u, v, w]` represents a directed edge from node `u` to node `v` with travel time `w`.

You are also given an integer `k`, the starting node. Return the minimum time it takes for all nodes to receive the signal from node `k`. If it is impossible, return `-1`.

### Examples
**Example 1:**
```
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Explanation: Signal travels from 2 → 1 (1), 2 → 3 (1), 3 → 4 (1). Max time = 2.
```

**Example 2:**
```
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
```

**Example 3:**
```
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
Explanation: Node 2 can't reach node 1.
```

### Constraints
- 1 <= k <= n <= 100
- 1 <= times.length <= 6000
- times[i].length == 3
- 1 <= u, v <= n
- 0 <= w <= 100

## 🧠 Pattern Recognition
**Graph Pattern:** Weighted directed graph, shortest path from one node to all others.

**Core Concept:** Dijkstra's algorithm (priority queue/min-heap) to find shortest path from source to all nodes.

## 💡 Solution Approaches
### 1. Dijkstra's Algorithm (Recommended)
- Use min-heap to always expand node with smallest current distance
- Track shortest distance to each node
- When all nodes reached, return max distance
- If any node unreachable, return -1
- Time: O(E log V), Space: O(V + E)

### 2. Bellman-Ford (for negative weights)
- Not needed here (all weights ≥ 0)

### 3. BFS (only if all weights = 1)
- Not optimal for weighted graph

## 📊 Complexity Analysis
| Approach   | Time      | Space   | Notes                |
|------------|-----------|---------|----------------------|
| Dijkstra   | O(E log V)| O(V+E)  | Best for positive weights |
| Bellman-Ford| O(VE)    | O(V)    | Not needed here      |

## 🔍 Edge Cases
- Disconnected nodes
- Multiple edges between same nodes
- Self-loops
- Large graphs

## 🎯 Interview Tips
- Dijkstra: Always expand node with min distance
- Use heapq for priority queue
- Track visited nodes to avoid cycles
- Return max distance among all reachable nodes
- If any node unreachable, return -1

## 🔗 Pattern Connections
- Previous: Kth Largest Element (heap)
- Related: Shortest Path, Minimum Spanning Tree, Bellman-Ford

---
**Trước khi code, hãy nghĩ: Nếu bạn phải truyền tín hiệu từ một node đến toàn bộ mạng, bạn sẽ chọn node nào để mở rộng trước?**