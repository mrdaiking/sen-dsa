"""
Day 27: Evaluate RPN
Leetcode Problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
"""

def evalRPN(tokens: list[str]) -> int:
    """
    Evaluate the RPN expression.
    Only implement function signature and docstring.
    """
    stack = []
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(x / y) if y != 0 else raise_(ValueError("Division by zero"))
    }
    for token in tokens:
        if token in operators:
            # pop all number and calculate
            if len(stack) < 2:
                raise ValueError("Invalid RPN expression")
            b, a = stack.pop(), stack.pop()
            stack.append(operators[token](a, b))
        else:
            try:
                stack.append(int(token))
            except ValueError:
                raise ValueError(f"Invalid token: {token}")

    if len(stack) != 1:
        raise ValueError("Invalid RPN expression")
    return stack[0]

# Example usage:
if __name__ == "__main__":
    test_cases = [
        ["2", "1", "+", "3", "*"],  # 9
        ["4", "13", "5", "/", "+"],  # 6
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],  # 22
        ["-2", "3", "+"],  # 1
    ]
    for tokens in test_cases:
        print(f"{tokens}: {evalRPN(tokens)}")