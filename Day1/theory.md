# 📅 Day 1 Theory: Big-O & Array Operations

## 🎯 Learning Objectives
- Understand Big-O notation and its practical applications
- Master fundamental array operations and their complexities
- Recognize common patterns in array-based problems

---

## 📚 Big-O Notation Fundamentals

### What is Big-O?
Big-O describes the **worst-case** time/space complexity as input size approaches infinity. It helps us compare algorithm efficiency.

### Common Time Complexities (Best to Worst)

| Notation | Name | Example | Description |
|----------|------|---------|-------------|
| O(1) | Constant | Array access by index | Same time regardless of input size |
| O(log n) | Logarithmic | Binary search | Halves search space each step |
| O(n) | Linear | Single loop through array | Time grows linearly with input |
| O(n log n) | Linearithmic | Merge sort, heap sort | Efficient sorting algorithms |
| O(n²) | Quadratic | Nested loops | Time grows quadratically |
| O(2^n) | Exponential | Recursive fibonacci | Avoid if possible! |

### Visual Representation
```
Time
 |
 |     O(2^n)
 |    /
 |   /
 |  /     O(n²)
 | /     /
 |/     /
 |     /
 |    /     O(n log n)
 |   /     /
 |  /     /     O(n)
 | /     /     /
 |/     /     /
 |     /     /
 |    /     /     O(log n)
 |   /     /     /
 |  /     /     /
 | /     /     /
 |/     /     /     O(1)
 |_____/_____|_____________> Input Size (n)
```

---

## 🔄 Array Operations & Complexities

### Basic Operations
- **Access by index**: `arr[i]` → O(1)
- **Search for value**: Linear scan → O(n)
- **Insert at end**: `arr.append()` → O(1) amortized
- **Insert at beginning/middle**: Shift elements → O(n)
- **Delete from end**: `arr.pop()` → O(1)
- **Delete from beginning/middle**: Shift elements → O(n)

### Space Complexity
- **In-place operations**: O(1) extra space
- **Creating new array**: O(n) space
- **Recursive calls**: O(depth) space for call stack

---

## 🎯 Today's Problem Patterns

### 1. Two Sum Pattern
- **Brute Force**: Nested loops → O(n²)
- **Hash Map Optimization**: Trade space for time → O(n) time, O(n) space
- **Key Insight**: Lookup operations can be optimized with hash tables

### 2. Single Pass Optimization
- **Greedy Approach**: Make optimal choice at each step
- **State Tracking**: Keep track of min/max values seen so far
- **Key Insight**: Sometimes one pass is enough if you track the right variables

### 3. Two Pointers Technique
- **String/Array Processing**: Work from both ends toward center
- **Space Optimization**: Reduce O(n) space to O(1)
- **Key Insight**: Useful when you need to compare elements from different positions

---

## 🔍 Analysis Framework

When approaching any problem, ask yourself:

### Time Complexity Questions:
1. How many times do we iterate through the data?
2. What's the cost of each operation inside the loop?
3. Are there nested loops?
4. Can we reduce iterations with better data structures?

### Space Complexity Questions:
1. Do we create new data structures proportional to input size?
2. Can we solve it in-place?
3. What's the recursion depth (if applicable)?
4. Can we trade time for space or vice versa?

### Optimization Questions:
1. Is the data sorted? (Can we use binary search?)
2. Can we use hash tables for O(1) lookups?
3. Can we use two pointers to reduce space?
4. Is there a mathematical shortcut?

---

## ✅ Success Metrics for Today

By the end of Day 1, you should be able to:

1. **Explain** the time and space complexity of your solutions
2. **Identify** when to use hash maps vs other data structures
3. **Recognize** the two-pointers pattern
4. **Articulate** trade-offs between different approaches
5. **Think aloud** your problem-solving process

---

## 🎯 Ready for Practice?

Now that we've covered the theory, let's apply these concepts to real problems. Remember:

- **Think before coding** - always discuss your approach first
- **Explain your reasoning** - practice talking through your thought process  
- **Consider multiple solutions** - what are the trade-offs?
- **Analyze complexity** - can you do better?

Let's start with our first problem! 🚀