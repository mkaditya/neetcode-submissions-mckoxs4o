class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0] # own stock
        free_to_buy = 0 # no stock, free to buy
        cooldown = 0 # just sold, in cooldown

        for price in prices[1:]:
            prev_hold, prev_free, prev_cooldown = hold, free_to_buy, cooldown

            # can enter free_to_buy from prev_free or cooldown state, choose optimal
            free_to_buy = max(prev_free, prev_cooldown)

            # can hold stock if I bough previously or if I bought it now, what is better
            hold = max(prev_hold, prev_free - price)

            # can enter coold down, if I sell the stock (which happens only in hold state).
            cooldown = prev_hold + price

        return max(free_to_buy, hold, cooldown)