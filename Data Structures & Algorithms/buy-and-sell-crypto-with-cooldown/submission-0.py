class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Rest --(buy-py)---> Hold
        |                      |
        (cooldown)             |
        Sold----Sell(+px)------   


                         buy (-price)
 buy (-price)
      ┌─────────────────────────────┐
      ↓                             │
    HOLD  ──── sell (+price) ────→ SOLD
      │                             │
      │ (keep holding)              │ (cooldown)
      └──────────────┐              ↓
                     │            REST
                     │              │
                     │              │ (keep resting)
                     └──────────────┘
        """   

        hold = float("-inf")
        sold = rest = 0

        for price in prices:
            hold = max(hold, rest - price) # keep holding, or buy today
            rest = max(rest, sold) # do nothing, or sell things
            sold = hold + price # sell today from hold
        return max(sold, rest)