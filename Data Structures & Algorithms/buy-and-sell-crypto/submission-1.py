class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        
        buy, max_profit = prices[0], 0

        for idx in range(1, len(prices)):
            if prices[idx] < buy:
                buy = prices[idx]   
            else:
                profit = prices[idx] - buy
                max_profit = max(max_profit, profit)
        
        return max_profit

        
