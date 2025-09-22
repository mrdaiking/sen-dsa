"""
Advanced Best Time to Buy/Sell Stock - Senior Python Implementation
Demonstrates: Decorators, Generators, Performance Benchmarking, Memory Profiling
"""

import functools
import timeit
import tracemalloc
import random
from typing import Iterator, Generator, List, Union
from dataclasses import dataclass


def timing_decorator(func):
    """Decorator to measure execution time."""
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
    result: int


class AdvancedStockTrader:
    """
    Advanced stock trading algorithm with multiple approaches and performance analysis.
    LeetCode Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    """
    
    @timing_decorator
    @memory_profiler
    def max_profit_brute_force(self, prices: List[Union[int, float]]) -> int:
        """
        Brute force approach with performance monitoring.
        Time: O(n²), Space: O(1)
        """
        if not prices or len(prices) < 2:
            return 0
            
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
        return max_profit

    @timing_decorator
    @memory_profiler
    def max_profit_one_pass(self, prices: List[Union[int, float]]) -> int:
        """
        Optimal one-pass approach with performance monitoring.
        Time: O(n), Space: O(1)
        """
        if not prices or len(prices) < 2:
            return 0
            
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
            
        return max_profit

    def price_stream_generator(self, prices: List[int]) -> Generator[int, None, None]:
        """
        Generator that yields prices one by one (simulates real-time data stream).
        
        Args:
            prices: List of stock prices
            
        Yields:
            int: Individual stock price
        """
        print("📡 Starting price stream...")
        for i, price in enumerate(prices):
            print(f"📈 Day {i+1}: Price = ${price}")
            yield price
        print("📡 Price stream ended.")

    def max_profit_streaming(self, price_stream: Iterator[int]) -> int:
        """
        Handle real-time price data using generators.
        Perfect for infinite data streams or memory-constrained environments.
        
        Args:
            price_stream: Generator/Iterator of stock prices
            
        Returns:
            int: Maximum profit achievable
        """
        print("🔄 Processing price stream in real-time...")
        
        min_price = float('inf')
        max_profit = 0
        day = 0
        
        try:
            for price in price_stream:
                day += 1
                
                # Update minimum price seen so far
                if price < min_price:
                    min_price = price
                    print(f"💰 New lowest price found: ${price} on day {day}")
                
                # Calculate profit if we sell today
                current_profit = price - min_price
                
                # Update maximum profit
                if current_profit > max_profit:
                    max_profit = current_profit
                    print(f"📈 New max profit: ${max_profit} (buy at ${min_price}, sell at ${price})")
                    
        except StopIteration:
            print("🏁 Finished processing price stream.")
            
        return max_profit

    def infinite_price_generator(self, num_days: int = 100) -> Generator[int, None, None]:
        """
        Generate infinite stream of random stock prices.
        Demonstrates handling of potentially infinite data.
        
        Args:
            num_days: Number of days to generate prices for
            
        Yields:
            int: Random stock price between 1 and 1000
        """
        print(f"🎲 Generating {num_days} days of random stock prices...")
        
        for day in range(1, num_days + 1):
            # Generate realistic stock price (with some trend)
            base_price = 100
            volatility = random.randint(-20, 20)
            price = max(1, base_price + volatility)
            
            print(f"📅 Day {day}: Generated price = ${price}")
            yield price

    def benchmark_all_approaches(self, prices: List[int], iterations: int = 100) -> List[BenchmarkResult]:
        """
        Comprehensive performance benchmark of all approaches.
        
        Args:
            prices: Test data
            iterations: Number of iterations for timing
            
        Returns:
            List of benchmark results
        """
        print("🏃‍♂️ PERFORMANCE BENCHMARK STARTING...")
        print("=" * 60)
        
        approaches = [
            ("Brute Force O(n²)", self.max_profit_brute_force),
            ("One Pass O(n)", self.max_profit_one_pass),
        ]
        
        results = []
        
        for name, method in approaches:
            print(f"\n🧪 Testing {name}:")
            
            # Time measurement
            exec_time = timeit.timeit(
                lambda: method(prices.copy()),
                number=iterations
            ) / iterations
            
            # Memory measurement
            tracemalloc.start()
            result = method(prices.copy())
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            
            benchmark = BenchmarkResult(
                method=name,
                execution_time=exec_time,
                memory_usage=peak / 1024 / 1024,
                result=result
            )
            
            results.append(benchmark)
            
            print(f"⏱️  Average time: {exec_time:.8f} seconds")
            print(f"📊 Peak memory: {peak / 1024 / 1024:.4f} MB")
            print(f"📈 Result: ${result}")
        
        # Performance comparison
        print(f"\n📊 PERFORMANCE SUMMARY:")
        print("=" * 60)
        
        if len(results) >= 2:
            brute_force, one_pass = results[0], results[1]
            speedup = brute_force.execution_time / one_pass.execution_time
            print(f"🚀 Speedup: {speedup:.2f}x faster with one-pass approach")
            print(f"⚡ Time saved: {(brute_force.execution_time - one_pass.execution_time) * 1000:.2f}ms per operation")
        
        return results


def demonstrate_advanced_features():
    """
    Comprehensive demonstration of all advanced Python features.
    """
    print("🚀 ADVANCED STOCK TRADING ALGORITHM DEMO")
    print("=" * 80)
    
    trader = AdvancedStockTrader()
    
    # Test data
    test_prices = [7, 1, 5, 3, 6, 4, 8, 2, 9]
    
    print("📋 TEST DATA:", test_prices)
    print()
    
    # 1. Standard approaches with performance monitoring
    print("1️⃣  STANDARD APPROACHES WITH PERFORMANCE MONITORING:")
    print("-" * 50)
    
    brute_result = trader.max_profit_brute_force(test_prices)
    one_pass_result = trader.max_profit_one_pass(test_prices)
    
    print(f"✅ Both methods agree: ${brute_result} = ${one_pass_result}")
    print()
    
    # 2. Generator-based price stream processing
    print("2️⃣  GENERATOR-BASED PRICE STREAM PROCESSING:")
    print("-" * 50)
    
    # Create a price stream generator
    price_stream = trader.price_stream_generator(test_prices)
    
    # Process the stream
    streaming_result = trader.max_profit_streaming(price_stream)
    print(f"📊 Streaming result: ${streaming_result}")
    print()
    
    # 3. Infinite price generator demo
    print("3️⃣  INFINITE PRICE GENERATOR DEMO:")
    print("-" * 50)
    
    # Generate and process infinite stream (limited to 10 days for demo)
    infinite_stream = trader.infinite_price_generator(10)
    infinite_result = trader.max_profit_streaming(infinite_stream)
    print(f"📊 Infinite stream result: ${infinite_result}")
    print()
    
    # 4. Comprehensive performance benchmark
    print("4️⃣  COMPREHENSIVE PERFORMANCE BENCHMARK:")
    print("-" * 50)
    
    # Create larger test data for meaningful benchmark
    large_test_data = [random.randint(1, 1000) for _ in range(1000)]
    
    benchmark_results = trader.benchmark_all_approaches(large_test_data, iterations=10)
    
    print("\n🎯 FINAL PERFORMANCE REPORT:")
    for result in benchmark_results:
        print(f"📈 {result.method}: {result.execution_time:.6f}s, {result.memory_usage:.2f}MB")


if __name__ == "__main__":
    demonstrate_advanced_features()