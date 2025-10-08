"""
Day 17 - Best Time to Buy and Sell Stock (Sliding Window)
Leetcode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Given an array prices where prices[i] is the price of a given stock on the ith day,
return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
You must buy the stock before you sell it. You are only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock).
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.     
"""


def maxProfit(prices):
    if len(prices) < 2:
        return 0
    min_price, max_profit = prices[0], 0
    for i, price in enumerate(prices):
        # print(f'price: {price}')
        min_price = min(price, min_price)
        # print(f'min_price: {min_price}')
        max_profit = max(price - min_price, max_profit)
        # print(f'max_profit: {max_profit}')
    return max_profit

# Test cases
if __name__ == "__main__":
    tests = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
        ([1,2,3,4,5], 4),
        ([2,4,1], 2),
        ([3,3,3,3], 0),
        ([1], 0),
        ([], 0),
    ]
    # tests = [
    #     ([7,1,5,3,6,4], 5)
    # ]
    for prices, expected in tests:
        result = maxProfit(prices)
        print(f"Input: prices={prices} | Output: {result} | Expected: {expected}")
