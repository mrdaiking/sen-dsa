# Day 31: Binary Tree Level Order Traversal

## 🎯 Problem Statement
Given the root of a binary tree, return the **level order traversal** of its nodes' values. (i.e., from left to right, level by level).

## 🧠 Approach

### BFS (Breadth-First Search) with Queue
Unlike DFS (recursion) used in previous days, this requires **level-by-level traversal**:

**Algorithm:**
1. Use a **queue** (FIFO) to process nodes level by level
2. For each level:
   - Track number of nodes at current level (`level_size = len(queue)`)
   - Process all nodes at this level using a for loop
   - Add their children to queue for next level
3. Store each level's values in a list
4. Return list of lists

**Key Difference from DFS:**
- **DFS**: Goes deep (root → leaf) using recursion/stack
- **BFS**: Goes wide (level by level) using queue

## 📊 Complexity Analysis
- **Time**: O(n) - visit each node once
- **Space**: O(w) - queue holds max width of tree (worst case: full last level = n/2)

## 🔑 Key Insights
- **Queue-based traversal**: FIFO ensures level-by-level processing
- **Level tracking**: Count nodes at each level before processing
- **BFS vs DFS**: Different traversal orders for different use cases

## 🎯 Pattern Recognition
When you see:
- "Level by level"
- "Layer by layer"
- "By depth"
- "Shortest path in tree"

→ Think **BFS with Queue**

## 💻 Implementation
```python
from collections import deque

def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level_values = []
        
        for i in range(level_size):
            node = queue.popleft()
            level_values.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level_values)
    
    return result
```