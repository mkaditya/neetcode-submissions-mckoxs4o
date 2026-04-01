class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        possible_profits = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        return sum(p for p in possible_profits if p > 0)

        # max_profit = 0
        # sum_so_far = 0
        # for profit in possible_profits:
        #     if sum_so_far < 0:
        #         sum_so_far = 0
            
        #     sum_so_far = sum_so_far + profit
        #     max_profit = max(max_profit, sum_so_far)
        
        # return max_profit
            