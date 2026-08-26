class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')

        for idx, price in enumerate(prices):
            if price <= min_price:
                min_price = price
            max_profit = max(max_profit, price - min_price)
        return max_profit