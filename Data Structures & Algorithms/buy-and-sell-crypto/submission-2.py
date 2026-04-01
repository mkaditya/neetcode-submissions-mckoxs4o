class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy_price = float('inf')
        max_profit = 0

        for price in prices:
            profit = price - best_buy_price
            if profit < 0:
                best_buy_price = price
            max_profit = max(max_profit, profit)

        return max_profit