class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            free_to_buy -> buy (may be you think market is at low point)
                        -> do-nothing (may be you think market is at high point )

            hold -> sell (lock in profit)
                 -> do-nothing (look for future)
            
            sold -> cool (forced after buy)
            cool -> free_to_buy (time passes)

          do-nothing ->   free_to_buy -> do-noting -> buy
          cool->  free_to_buy -> buy
        """
        free_to_buy = 0 # has clearence to buy
        hold = -prices[0] # looking for good sell
        cooldown = 0 # mandatory rest

        for price in prices[1:]:
            prev_hold, prev_free, prev_cooldown = hold, free_to_buy, cooldown

            free_to_buy = max(prev_free, prev_cooldown)
            hold = max(prev_hold, prev_free - price)
            cooldown = prev_hold + price

        return max(free_to_buy, hold, cooldown)