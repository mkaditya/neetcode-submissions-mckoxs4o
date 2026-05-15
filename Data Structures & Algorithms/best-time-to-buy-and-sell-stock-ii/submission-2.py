class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            two states: no_stock, has_stock

            no_stock -> no_stock 
            no_stock -buy-> has_stack

            has_stack -sell-> no_stock
        """
        profit = 0
    
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1] >= 0:
                profit += (prices[i] - prices[i-1])
        return profit # we will sell things.