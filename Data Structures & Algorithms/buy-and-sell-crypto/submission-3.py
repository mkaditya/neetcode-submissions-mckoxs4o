class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for sell in prices:
            max_profit = max(max_profit, sell - buy)
            if sell < buy:
                buy = sell
        return max_profit