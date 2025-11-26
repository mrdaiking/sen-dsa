# 📚 **Day 38: Course Schedule (Topological Sort)**

## 🎯 Problem Statement

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must take course `bi` first if you want to take course `ai`**.

For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

### Examples

**Example 1:**
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are 2 courses. To take course 1, you need to take course 0.
```

**Example 2:**
```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: To take course 1, you need course 0, and to take course 0, you need course 1. It's a circular dependency!
```

**Example 3:**
```
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: true
Explanation: Valid order: [0,1,2,3] or [0,2,1,3]
```

### Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- All pairs in `prerequisites` are unique

## 🧠 Pattern Recognition

**Graph Pattern:** This is a **Directed Acyclic Graph (DAG)** problem.

**Core Concept:** 
- Each course is a **node**
- Each prerequisite is a **directed edge**: `[a, b]` means `b → a` (b must come before a)
- Question becomes: **Does the graph have a cycle?**

**Key Insight:** You can finish all courses **IF AND ONLY IF** there's no cycle in the dependency graph.

## 💡 Solution Approaches

### 1. DFS - Cycle Detection (Recommended)
- Use 3 states: **unvisited**, **visiting**, **visited**
- If we revisit a **visiting** node → cycle detected
- Time: O(V + E), Space: O(V)

### 2. BFS - Kahn's Algorithm (Topological Sort)
- Count in-degrees for each node
- Process nodes with in-degree = 0
- Remove edges and update in-degrees
- If processed all nodes → no cycle
- Time: O(V + E), Space: O(V)

### 3. Union-Find (Less optimal)
- Track connected components
- Time: O(E × α(V)), not ideal for directed graphs

## 📊 Complexity Analysis

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| DFS | O(V + E) | O(V) | Most intuitive, direct cycle detection |
| BFS (Kahn's) | O(V + E) | O(V) | Also gives topological order |
| Union-Find | O(E × α) | O(V) | Not ideal for directed graphs |

Where V = numCourses, E = prerequisites.length

## 🔍 Key Concepts

### **3-State DFS Pattern:**
- **0 (Unvisited):** Not explored yet
- **1 (Visiting):** Currently in DFS path (gray node)
- **2 (Visited):** Completely processed (black node)

**Cycle detection:** If we encounter a **visiting (1)** node during DFS → cycle!

### **Topological Sort:**
- Linear ordering of vertices where every directed edge u → v: u comes before v
- Only possible in DAG (no cycles)
- Multiple valid orderings possible

## 🔍 Edge Cases

- No prerequisites: `[]` → always true
- Self-loop: `[[0,0]]` → false (cycle)
- Simple cycle: `[[1,0],[0,1]]` → false
- Disconnected graph: Multiple independent course chains → true
- Single course: `numCourses = 1, prerequisites = []` → true

## 🎯 Interview Tips

- **Recognize:** Keywords like "dependency", "prerequisite", "order" → Graph problem
- **Cycle detection:** Core skill for many graph problems
- **State tracking:** 3-state pattern is powerful for DFS cycle detection
- **Build adjacency list:** Don't use matrix for sparse graphs
- **Direction matters:** `[a, b]` means b → a (b before a)

## 🔗 Pattern Connections

- **Previous:** Number of Islands (graph traversal on grid)
- **Next:** Network Delay Time (weighted graph, Dijkstra)
- **Related:** Course Schedule II (return topological order), Alien Dictionary

---

## 🤔 **Thinking Questions**

Trước khi nhìn code, hãy nghĩ:

1. **Bài toán này về bản chất là gì?** (Hint: cycle detection)
2. **Làm sao biết có cycle?** (Hint: gặp lại node đang thăm)
3. **Cần lưu trữ gì?** (Hint: adjacency list + state array)
4. **DFS hay BFS?** (Hint: cả hai đều được, nhưng DFS ngắn gọn hơn)

**Bạn sẽ tiếp cận bài này như thế nào?**