import re
from dataclasses import dataclass

def timing_decorator(func):
    """Decorator to measure execution time."""
    import timeit
    import functools

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        print(f"⏱️  {func.__name__} executed in {end_time - start_time:.6f} seconds")
        return result
    return wrapper

def memory_profiler(func):
    """Decorator to measure memory usage."""
    import tracemalloc
    import functools

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"📊 {func.__name__} - Peak memory: {peak / 1024 / 1024:.2f} MB")
        return result
    return wrapper

@dataclass
class BenchmarkResult:
    """Store benchmark results."""
    method: str
    execution_time: float
    memory_usage: float
    result: str
    
class ValidPalindrome:
    """LeetCode 125: Valid Palindrome
    https://leetcode.com/problems/valid-palindrome/
    """
    @timing_decorator
    @memory_profiler
    def is_palindrome_approach1(self, s):
        """ Two-pointer technique:
            1. Clean the string by removing non-alphanumeric characters and converting to lowercase.
            2. Use two pointers to check for palindrome.
            Time complexity: O(n)
            Space complexity: O(1)
            Args:
                s (str): Input string.
            Returns:
                bool: True if s is a palindrome, False otherwise.
            Raises:
                TypeError: If input is not a string.
            """
    
        # Step 1: filter and normalize
        try:
            if not isinstance(s, str):
                raise TypeError("Input must be a string.")
        except TypeError as e:
            raise TypeError(f"Input must be a string. {str(e)}")
        
        cleaned = self.remove_non_alphanumeric(s).lower()
        print(f"Cleaned string: {cleaned}")
        left, right = 0, len(cleaned) - 1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left+=1
            right-=1
        return True
    

    
    @timing_decorator
    @memory_profiler
    def remove_non_alphanumeric(self, s: str) -> str:
        """Remove non-alphanumeric characters from the string."""
        return re.sub(r'[^a-zA-Z0-9]', '', s)
    

def main():
    vp = ValidPalindrome()
    test_strings = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
        "No 'x' in Nixon"
    ]
    for s in test_strings:
        print(f"Is the string a palindrome? {vp.is_palindrome_approach1(s)}")


if __name__ == "__main__":
    main()