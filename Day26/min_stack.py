"""
Day 26: Min Stack
Leetcode Problem: https://leetcode.com/problems/min-stack/
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
"""

class MinStack:
    def __init__(self):
        """Initialize your data structure here."""
        self.stack = []
        self.min_stack = []
        pass

    def push(self, val: int) -> None:
        """Push element x onto stack."""
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """Removes the element on top of the stack."""
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()


    def top(self) -> int:
        """Get the top element."""
        return self.stack[-1]

    def getMin(self) -> int:
        """Retrieve the minimum element in the stack."""
        return self.min_stack[-1]

# Example usage:
if __name__ == "__main__":
    stack = MinStack()
    stack.push(5)
    stack.push(2)
    stack.push(4)
    stack.push(1)
    print("Top:", stack.top())      # Should print 1
    print("Min:", stack.getMin())   # Should print 1
    stack.pop()
    print("Top:", stack.top())      # Should print 4
    print("Min:", stack.getMin())   # Should print 2
    stack.pop()
    print("Top:", stack.top())      # Should print 2
    print("Min:", stack.getMin())   # Should print 2
