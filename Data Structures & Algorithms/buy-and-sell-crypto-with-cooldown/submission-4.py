class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Three States:
            no_stock
            has_stock
            cooldown 

        State Transitions:
            no_stock --buy stock --> has_stock
            no_stock --do nothing --> no_stock

            has_stock --do noting --> has_stock
            has_stock --sell stock --> cooldown

            cooldown --> no_stock
            cooldown --> cooldown

        Goal:
            optimize sell - buy
        """

        # first day possible states
        no_stock = 0 
        cooldown = 0 # nobody sold anything yet
        has_stock = -prices[0] # signifies buying on first day

        for price in prices[1:]:
            # capture previous states for state transitions
            prev_no_stock, prev_cooldown, prev_has_stock = no_stock, cooldown, has_stock

            # no stock can be entered from no_stock or cooldown
            # we want enter with max value into it
            no_stock = max(prev_no_stock, prev_cooldown)

            # has stock can be entered from has_stock (doing nothing) or no_stock(buying)
            # doing max for accounnting min value through negation of price
            has_stock = max(prev_has_stock, prev_no_stock - price)

            # cooldown can be entered by only has_stock & selling or from cooldown state itself
            cooldown = max (prev_cooldown, prev_has_stock + price)

        return max(cooldown, no_stock) # we want to sell stuff towards the end not hold stocks