

from dataclasses import dataclass


class BestBuySell:
    """
    You are given an array `prices` where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy the stock and 
    a different day in the future to sell it.

    Return the maximum profit you can achieve from this transaction. 
    If you cannot achieve any profit, return 0.

    Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that you cannot sell on day 1 (price = 7) and then buy on day 2 (price = 1).

    Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.
    """

    def max_profit_brute_force(self, prices: list[int]) -> int:
        """
        Brute force: check all pairs (i, j) where i < j
        Time complexity: O(n^2)
        Space complexity: O(1)
        Args:
            prices (list[int]): List of stock prices.
        Returns:
            int: Maximum profit achievable.
        """
        try:
            if not isinstance(prices, list) or not prices:
                raise ValueError("Input must be a non-empty list")
            if not all(isinstance(price, (int, float)) for price in prices):
                raise TypeError("All elements in prices must be integers or floats.")
            
            max_profit = 0
            for i in range(len(prices)):
                for j in range(i+1, len(prices)):
                    profit = prices[j] - prices[i]
                    max_profit = max(max_profit, profit)
        except Exception as e:
            raise ValueError(f"An error occurred: {str(e)}")
        return max_profit

    def max_profit_one_pass(self, prices: list[int]) -> int:
        """
        One-pass approach:
        Track min_price và max_profit as we go
        Time complexity: O(n)
        Space complexity: O(1)
        Args:
            prices (list[int]): List of stock prices.
        Returns:
            int: Maximum profit achievable.
        """
        try:
            if not isinstance(prices, list) or not prices:
                raise ValueError("Input must be a non-empty list")
            if not all(isinstance(price, (int, float)) for price in prices):
                raise TypeError("All elements in prices must be integers or floats.")
            min_price = float('inf')
            max_profit = 0

            for price in prices:
                # Update minimum price seen so far
                min_price = min(min_price, price)
                # Calculate profit if we sell today
                profit = price - min_price
                # Update maximum profit
                max_profit = max(max_profit, profit)
        except Exception as e:
            raise ValueError(f"An error occurred: {str(e)}")
        return max_profit


    

def main():
    prices1 = [7, 1, 5, 3, 6, 4]
    prices2 = [7, 6, 4, 3, 1]

    solver = BestBuySell()

    print("Brute Force Approach:")
    print(f"Max profit for {prices1}: {solver.max_profit_brute_force(prices1)}")  # Output: 5
    print(f"Max profit for {prices2}: {solver.max_profit_brute_force(prices2)}")  # Output: 0

    print("\nOne-Pass Approach:")
    print(f"Max profit for {prices1}: {solver.max_profit_one_pass(prices1)}")  # Output: 5
    print(f"Max profit for {prices2}: {solver.max_profit_one_pass(prices2)}")  # Output: 0

if __name__ == "__main__":
    main()
