"""
Advanced Two Sum Implementation - Senior Python Developer Level

This module demonstrates advanced Python concepts:
- Multiple solution approaches
- Performance benchmarking
- Memory profiling
- Type hints with Union types
- Decorators for timing
- Class-based design patterns
- List comprehensions where applicable
"""

from typing import List, Union, Optional, Tuple, Iterator
import timeit
import random
import functools
import tracemalloc
from dataclasses import dataclass
from enum import Enum
import sys


class SolutionMethod(Enum):
    """Enumeration of available solution methods."""
    HASH_MAP = "hash_map"
    BRUTE_FORCE = "brute_force"
    SORTED_TWO_POINTERS = "sorted_two_pointers"
    LIST_COMPREHENSION = "list_comprehension"


@dataclass
class BenchmarkResult:
    """Data class for storing benchmark results."""
    method: str
    execution_time: float
    memory_usage: float
    result: List[int]


def timing_decorator(func):
    """Decorator to measure execution time of functions."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        print(f"{func.__name__} executed in {end_time - start_time:.6f} seconds")
        return result
    return wrapper


def memory_profiler(func):
    """Decorator to measure memory usage of functions."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"{func.__name__} - Current memory: {current / 1024 / 1024:.2f} MB, Peak: {peak / 1024 / 1024:.2f} MB")
        return result
    return wrapper


class TwoSumSolutions:
    """
    Advanced Two Sum implementation with multiple solution approaches.
    
    This class demonstrates various Python advanced concepts and provides
    different algorithmic approaches for solving the Two Sum problem.
    LeetCode Problem: https://leetcode.com/problems/two-sum/
    """
    
    @staticmethod
    @timing_decorator
    @memory_profiler
    def hash_map_optimal(nums: List[Union[int, float]], target: Union[int, float]) -> List[int]:
        """
        Optimal O(n) time, O(n) space solution using hash map.
        
        Args:
            nums: List of numbers
            target: Target sum
            
        Returns:
            List containing indices of two numbers that sum to target
            
        Raises:
            ValueError: If input validation fails
            TypeError: If types are incorrect
        """
        if not isinstance(nums, list) or not nums:
            raise ValueError("Input must be a non-empty list")
        
        if not isinstance(target, (int, float)):
            raise TypeError("Target must be a number")
            
        seen = {}
        for i, num in enumerate(nums):
            if not isinstance(num, (int, float)):
                raise TypeError(f"All elements must be numbers. Found {type(num)} at index {i}")
            
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        
        return []
    
    @staticmethod
    @timing_decorator
    @memory_profiler
    def brute_force(nums: List[Union[int, float]], target: Union[int, float]) -> List[int]:
        """
        O(n²) time, O(1) space brute force solution.
        
        Args:
            nums: List of numbers
            target: Target sum
            
        Returns:
            List containing indices of two numbers that sum to target
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    @staticmethod
    @timing_decorator
    @memory_profiler
    def list_comprehension_approach(nums: List[Union[int, float]], target: Union[int, float]) -> List[int]:
        """
        Creative list comprehension approach (still O(n²) but Pythonic).
        
        Args:
            nums: List of numbers
            target: Target sum
            
        Returns:
            List containing indices of two numbers that sum to target
        """
        try:
            return next(
                [i, j] for i in range(len(nums)) 
                for j in range(i + 1, len(nums)) 
                if nums[i] + nums[j] == target
            )
        except StopIteration:
            return []
    
    @staticmethod
    @timing_decorator
    @memory_profiler
    def sorted_two_pointers(nums: List[Union[int, float]], target: Union[int, float]) -> List[int]:
        """
        Two pointers approach on sorted array with index tracking.
        O(n log n) time due to sorting, O(n) space.
        
        Args:
            nums: List of numbers
            target: Target sum
            
        Returns:
            List containing original indices of two numbers that sum to target
        """
        # Create list of (value, original_index) pairs
        indexed_nums = [(nums[i], i) for i in range(len(nums))]
        indexed_nums.sort(key=lambda x: x[0])  # Sort by value
        
        left, right = 0, len(indexed_nums) - 1
        
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            
            if current_sum == target:
                # Return original indices in ascending order
                indices = sorted([indexed_nums[left][1], indexed_nums[right][1]])
                return indices
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []
    
    @classmethod
    def benchmark_all_methods(cls, nums: List[Union[int, float]], target: Union[int, float], 
                            iterations: int = 1000) -> List[BenchmarkResult]:
        """
        Benchmark all solution methods and return performance metrics.
        
        Args:
            nums: Test input array
            target: Target sum
            iterations: Number of iterations for timing
            
        Returns:
            List of BenchmarkResult objects with performance data
        """
        methods = {
            'hash_map_optimal': cls.hash_map_optimal,
            'brute_force': cls.brute_force,
            'list_comprehension': cls.list_comprehension_approach,
            'sorted_two_pointers': cls.sorted_two_pointers
        }
        
        results = []
        
        for method_name, method_func in methods.items():
            print(f"\n--- Benchmarking {method_name} ---")
            
            # Time measurement
            execution_time = timeit.timeit(
                lambda: method_func(nums.copy(), target),
                number=iterations
            ) / iterations
            
            # Memory measurement
            tracemalloc.start()
            result = method_func(nums.copy(), target)
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            
            benchmark_result = BenchmarkResult(
                method=method_name,
                execution_time=execution_time,
                memory_usage=peak / 1024 / 1024,  # Convert to MB
                result=result
            )
            
            results.append(benchmark_result)
            
            print(f"Average execution time: {execution_time:.8f} seconds")
            print(f"Peak memory usage: {peak / 1024 / 1024:.4f} MB")
            print(f"Result: {result}")
        
        return results


class AdvancedTwoSum:
    """
    Advanced wrapper class with additional utility methods.
    """
    
    def __init__(self):
        self.solutions = TwoSumSolutions()
    
    def generate_test_data(self, size: int = 1000, value_range: Tuple[int, int] = (-1000, 1000)) -> Tuple[List[int], int]:
        """
        Generate random test data for benchmarking.
        
        Args:
            size: Size of the array
            value_range: Range of values (min, max)
            
        Returns:
            Tuple of (nums array, target) where solution is guaranteed to exist
        """
        nums = random.sample(range(value_range[0], value_range[1]), size)
        # Ensure solution exists by using sum of first and last elements
        target = nums[0] + nums[-1]
        return nums, target
    
    def performance_comparison(self, input_sizes: List[int] = None):
        """
        Compare performance across different input sizes.
        
        Args:
            input_sizes: List of input sizes to test
        """
        if input_sizes is None:
            input_sizes = [100, 500, 1000, 2000]
        
        print("=" * 80)
        print("PERFORMANCE COMPARISON ACROSS INPUT SIZES")
        print("=" * 80)
        
        for size in input_sizes:
            print(f"\n{'='*20} INPUT SIZE: {size} {'='*20}")
            nums, target = self.generate_test_data(size)
            
            # Only test efficient methods for large inputs
            if size <= 1000:
                self.solutions.benchmark_all_methods(nums, target, iterations=100)
            else:
                print("Testing only efficient methods for large input...")
                result = self.solutions.hash_map_optimal(nums, target)
                print(f"Hash map result: {result}")


def main():
    """
    Demonstrate advanced Two Sum implementation with comprehensive testing.
    """
    print("🚀 ADVANCED TWO SUM - SENIOR PYTHON DEVELOPER IMPLEMENTATION")
    print("=" * 80)
    
    # Initialize advanced two sum
    advanced_solver = AdvancedTwoSum()
    
    # Test with sample data
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([-1, -2, -3, -4, -5], -8),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 17)
    ]
    
    print("\n📋 TESTING ALL METHODS WITH SAMPLE DATA:")
    for i, (nums, target) in enumerate(test_cases, 1):
        print(f"\n--- Test Case {i}: nums={nums}, target={target} ---")
        
        # Test all methods
        try:
            hash_result = TwoSumSolutions.hash_map_optimal(nums.copy(), target)
            brute_result = TwoSumSolutions.brute_force(nums.copy(), target)
            comp_result = TwoSumSolutions.list_comprehension_approach(nums.copy(), target)
            sorted_result = TwoSumSolutions.sorted_two_pointers(nums.copy(), target)
            
            print(f"Hash Map: {hash_result}")
            print(f"Brute Force: {brute_result}")
            print(f"List Comprehension: {comp_result}")
            print(f"Sorted Two Pointers: {sorted_result}")
            
            # Verify all methods return same result
            all_results = [hash_result, brute_result, comp_result, sorted_result]
            if len(set(map(tuple, all_results))) == 1:
                print("✅ All methods returned consistent results!")
            else:
                print("❌ Methods returned different results!")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    # Performance comparison
    print(f"\n⚡ PERFORMANCE BENCHMARK:")
    advanced_solver.performance_comparison([100, 500])
    
    print(f"\n🎯 MEMORY EFFICIENCY TEST:")
    large_nums, large_target = advanced_solver.generate_test_data(5000)
    print("Testing with 5000 elements...")
    result = TwoSumSolutions.hash_map_optimal(large_nums, large_target)
    print(f"Result for large dataset: {result}")


if __name__ == "__main__":
    main()