"""
LeetCode 125: Valid Palindrome - Advanced Implementation
Senior-level implementation with multiple approaches and performance benchmarking.
"""

import re
import timeit
import tracemalloc
from dataclasses import dataclass
from typing import List, Iterator, Union
from functools import wraps
from enum import Enum


class ApproachType(Enum):
    """Enumeration of different solution approaches."""
    FILTER_FIRST = "filter_first"
    TWO_POINTER_INLINE = "two_pointer_inline"
    GENERATOR_BASED = "generator_based"
    REGEX_OPTIMIZED = "regex_optimized"


def performance_monitor(func):
    """Enhanced decorator for comprehensive performance monitoring."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Memory tracking
        tracemalloc.start()
        
        # Time tracking
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        
        # Memory analysis
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        execution_time = end_time - start_time
        memory_mb = peak / 1024 / 1024
        
        print(f"🔍 {func.__name__}:")
        print(f"   ⏱️  Time: {execution_time:.6f}s")
        print(f"   📊 Peak Memory: {memory_mb:.3f} MB")
        print(f"   ✅ Result: {result}")
        print()
        
        return result
    return wrapper


@dataclass
class BenchmarkResult:
    """Comprehensive benchmark result storage."""
    approach: str
    execution_time: float
    memory_usage: float
    space_complexity: str
    time_complexity: str
    result: bool


class AdvancedValidPalindrome:
    """
    Advanced Valid Palindrome implementation with multiple optimization approaches.
    Demonstrates senior-level Python patterns and performance engineering.
    """
    
    @performance_monitor
    def approach1_filter_first(self, s: str) -> bool:
        """
        Your original approach: Filter first, then two-pointer check.
        
        Time Complexity: O(n)
        Space Complexity: O(n) - creates new string
        
        Pros: Simple, readable
        Cons: Uses extra O(n) space
        """
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
            
        # Filter and normalize
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        # Two-pointer check
        left, right = 0, len(cleaned) - 1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True
    
    @performance_monitor
    def approach2_optimized_space(self, s: str) -> bool:
        """
        Space-optimized approach: Check palindrome without creating new string.
        
        Time Complexity: O(n)
        Space Complexity: O(1) - no extra space!
        
        Pros: Optimal space usage
        Cons: Slightly more complex logic
        """
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
            
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric from left
            while left < right and not s[left].isalnum():
                left += 1
            
            # Skip non-alphanumeric from right  
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
            
        return True
    
    @performance_monitor
    def approach3_generator_based(self, s: str) -> bool:
        """
        Generator-based approach: Memory-efficient character streaming.
        
        Time Complexity: O(n)
        Space Complexity: O(n) - converts generator to list for two-pointer access
        
        Pros: Demonstrates advanced Python patterns
        Cons: Still creates O(n) list, not truly O(1)
        """
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
            
        def clean_chars() -> Iterator[str]:
            """Generator that yields only alphanumeric characters in lowercase."""
            for char in s:
                if char.isalnum():
                    yield char.lower()
        
        # Convert generator to list for two-pointer access - O(n) space!
        chars = list(clean_chars()) 
        
        left, right = 0, len(chars) - 1
        while left < right:
            if chars[left] != chars[right]:
                return False
            left += 1
            right -= 1
        return True
    
    @performance_monitor
    def approach5_true_streaming(self, s: str) -> bool:
        """
        True streaming approach: Real O(1) space with generators.
        
        Time Complexity: O(n)
        Space Complexity: O(1) - true streaming without storing characters
        
        Pros: Truly memory efficient, good for very large strings
        Cons: More complex implementation, multiple passes
        """
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
            
        def clean_chars_forward() -> Iterator[str]:
            """Generator for forward iteration."""
            for char in s:
                if char.isalnum():
                    yield char.lower()
                    
        def clean_chars_backward() -> Iterator[str]:
            """Generator for backward iteration."""
            for char in reversed(s):
                if char.isalnum():
                    yield char.lower()
        
        # Compare streams without storing
        forward_gen = clean_chars_forward()
        backward_gen = clean_chars_backward()
        
        try:
            while True:
                left_char = next(forward_gen)
                right_char = next(backward_gen)
                
                if left_char != right_char:
                    return False
        except StopIteration:
            # If both generators exhausted simultaneously, it's a palindrome
            return True
    
    @performance_monitor  
    def approach4_regex_optimized(self, s: str) -> bool:
        """
        Regex-optimized with compiled pattern for better performance.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Pros: Fastest regex processing, good for multiple calls
        Cons: Still uses O(n) space
        """
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
            
        # Compiled regex for better performance in repeated calls
        pattern = re.compile(r'[^a-zA-Z0-9]')
        cleaned = pattern.sub('', s).lower()
        
        # Pythonic palindrome check
        return cleaned == cleaned[::-1]


class PalindromeBenchmark:
    """Comprehensive benchmarking suite for palindrome algorithms."""
    
    def __init__(self):
        self.palindrome_solver = AdvancedValidPalindrome()
        self.test_cases = [
            "A man, a plan, a canal: Panama",
            "race a car", 
            " ",
            "No 'x' in Nixon",
            "Madam",
            "Was it a car or a cat I saw?",
            "12321",
            "hello world" * 100,  # Larger test case
        ]
    
    def run_comprehensive_benchmark(self) -> List[BenchmarkResult]:
        """Run all approaches and collect detailed benchmark results."""
        approaches = [
            ("Filter First (Your Approach)", self.palindrome_solver.approach1_filter_first, "O(n)", "O(n)"),
            ("Optimized Space", self.palindrome_solver.approach2_optimized_space, "O(n)", "O(1)"),
            ("Generator Based", self.palindrome_solver.approach3_generator_based, "O(n)", "O(n)"),
            ("Regex Optimized", self.palindrome_solver.approach4_regex_optimized, "O(n)", "O(n)"),
            ("True Streaming", self.palindrome_solver.approach5_true_streaming, "O(n)", "O(1)"),
        ]
        
        results = []
        
        print("🚀 COMPREHENSIVE PALINDROME ALGORITHM BENCHMARK")
        print("=" * 60)
        
        for test_case in self.test_cases[:3]:  # Test with first 3 cases
            print(f"\n📝 Testing: '{test_case}'")
            print("-" * 40)
            
            for name, method, time_comp, space_comp in approaches:
                try:
                    # Measure performance
                    tracemalloc.start()
                    start_time = timeit.default_timer()
                    
                    result = method(test_case)
                    
                    end_time = timeit.default_timer()
                    current, peak = tracemalloc.get_traced_memory()
                    tracemalloc.stop()
                    
                    benchmark_result = BenchmarkResult(
                        approach=name,
                        execution_time=end_time - start_time,
                        memory_usage=peak / 1024 / 1024,
                        time_complexity=time_comp,
                        space_complexity=space_comp,
                        result=result
                    )
                    results.append(benchmark_result)
                    
                except Exception as e:
                    print(f"❌ {name} failed: {e}")
        
        return results
    
    def performance_comparison(self):
        """Compare performance of different approaches."""
        print("\n🏆 PERFORMANCE COMPARISON SUMMARY")
        print("=" * 50)
        
        test_string = "A man, a plan, a canal: Panama" * 10  # Larger test
        
        approaches = {
            "Your Approach (Filter First)": self.palindrome_solver.approach1_filter_first,
            "Optimized Space O(1)": self.palindrome_solver.approach2_optimized_space,
            "Generator Based": self.palindrome_solver.approach3_generator_based,
            "Regex Optimized": self.palindrome_solver.approach4_regex_optimized,
            "True Streaming O(1)": self.palindrome_solver.approach5_true_streaming,
        }
        
        for name, method in approaches.items():
            print(f"\n🔍 {name}:")
            method(test_string)


def main():
    """Demonstrate all approaches with comprehensive analysis."""
    print("🎯 ADVANCED VALID PALINDROME IMPLEMENTATION")
    print("=" * 60)
    
    # Initialize benchmark suite
    benchmark = PalindromeBenchmark()
    
    # Run comprehensive benchmark
    benchmark.run_comprehensive_benchmark()
    
    # Performance comparison
    benchmark.performance_comparison()
    
    print("\n📚 KEY LEARNINGS:")
    print("✅ Approach 1 (Your method): Good for readability, O(n) space")
    print("✅ Approach 2 (Optimized): Best balance - O(1) space, readable")
    print("✅ Approach 3 (Generator): Advanced Python but still O(n) space")
    print("✅ Approach 4 (Regex): Good for multiple calls, O(n) space")
    print("✅ Approach 5 (True Streaming): Real O(1) space for huge datasets")
    
    print("\n🎯 INTERVIEW RECOMMENDATION:")
    print("Start with Approach 1 (clear), then optimize to Approach 2 (O(1) space)")
    print("For very large datasets: Consider Approach 5 (true streaming)")
    
    print("\n🏆 SPACE COMPLEXITY RANKING:")
    print("🥇 Approach 2 & 5: O(1) - True space optimization")
    print("🥈 Approach 1, 3, 4: O(n) - Create additional data structures")


if __name__ == "__main__":
    main()