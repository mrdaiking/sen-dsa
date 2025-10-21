'''
def isValid(s: str) -> bool:
    """
    Check if the input string of parentheses is valid.
    Only implement function signature and docstring.
    """
'''
def isValid(s: str) -> bool:
    """
    Check if the input string of parentheses is valid.
    Only implement function signature and docstring.
    """
    if len(s) == 0:
        return True
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for i, char in enumerate(s):
        if char in mapping.values(): # Add open racket
            stack.append(char)
        elif char in mapping:
            if not stack: # return False if stack empty
                return False
            
            if stack[-1] != mapping[char]: #check close racket is invalid
                return False
            
            stack.pop() # get valid open racket
        
    return len(stack) == 0


# Example usage:
if __name__ == "__main__":
    test_cases = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "",
        "([{}])",
    ]
    for s in test_cases:
        print(f"{s}: {isValid(s)}")

