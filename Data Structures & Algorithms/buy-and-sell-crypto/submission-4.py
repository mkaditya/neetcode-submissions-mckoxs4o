class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        States:
            no_stock, has_stock
        
        Transitions:
            no_stock --dont do anything--> no_stock
            no_stock --buy_stock ---> has_stock (only once)

            has_stock --don't do anything --> has_stock
            has_stock --sell_stock ---> no_stock (only once)

        End goal:
            What is maximum profit, in other words after we sell stock or don't do anything
            what is the amount we make
        """

        no_stock = 0
        has_stock = -prices[0]

        for price in prices:
            # capture state before transition
            prev_no_stock, prev_has_stock = no_stock, has_stock

            # you can enter into no_stock state by not doing anything from no stock
            # or by selling stock from has stock, of course we want to maximize profit
            no_stock = max(prev_no_stock, prev_has_stock + price)

            has_stock = max(prev_has_stock, -price) # idetify wha is best position to buy stock
        return no_stock