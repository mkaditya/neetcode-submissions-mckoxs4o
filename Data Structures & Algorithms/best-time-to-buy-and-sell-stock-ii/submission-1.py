class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            two states: no_stock, has_stock

            no_stock -> no_stock 
            no_stock -buy-> has_stack

            has_stack -sell-> no_stock
        """
        no_stock = 0
        has_stock = -prices[0] # bought the stock, which costs

        for price in prices[1:]:
            prev_no_stock, prev_has_stock = no_stock, has_stock

            no_stock = max(prev_no_stock, prev_has_stock + price) # sell the has_stack
            has_stock = max(prev_has_stock, prev_no_stock - price) # we always assume we bought for the best deal stock
        
        return no_stock