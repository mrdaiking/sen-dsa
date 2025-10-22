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
        if self.stack:
            if self.min_stack and self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()
        
    def top(self) -> int:
        """Get the top element."""
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        """Retrieve the minimum element in the stack."""
        return self.min_stack[-1] if self.min_stack else None

# Example usage:
if __name__ == "__main__":
    stack = MinStack()
    print(f"stack: {stack.stack}")
    print(f"min_stack: {stack.min_stack}")
    print("-" * 30)
    
    print("Push 5:")
    stack.push(5)
    print(f"stack: {stack.stack}")
    print(f"min_stack: {stack.min_stack}")
    print("-" * 30)
    
    print("Push 2:")
    stack.push(2)
    print(f"stack: {stack.stack}")
    print(f"min_stack: {stack.min_stack}")
    print("-" * 30)
    
    print("Push 4:")
    stack.push(4)
    print(f"stack: {stack.stack}")
    print(f"min_stack: {stack.min_stack}")
    print("-" * 30)
    
    print("Push 1:")
    stack.push(1)
    print(f"stack: {stack.stack}")
    print(f"min_stack: {stack.min_stack}")
    print("-" * 30)
    
    print("Pop (1):")
    stack.pop()
    print(f"stack: {stack.stack}")
    print(f"min_stack: {stack.min_stack}")
    print("-" * 30)
    
    print("Pop (4):")
    stack.pop()
    print(f"stack: {stack.stack}")
    print(f"min_stack: {stack.min_stack}")
    print("-" * 30)
    
    print("Pop (2):")
    stack.pop()
    print(f"stack: {stack.stack}")
    print(f"min_stack: {stack.min_stack}")
    print("-" * 30)
    
    print("Pop (5):")
    stack.pop()
    print(f"stack: {stack.stack}")
    print(f"min_stack: {stack.min_stack}")
    print("-" * 30)
