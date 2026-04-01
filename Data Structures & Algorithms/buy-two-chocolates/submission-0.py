class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1, min2 = float('inf'), float('inf')

        for price in prices:
            if price < min1:
                min1, min2 = price, min1
            elif price < min2:
                min2 = price
        
        leftover_money = money - (min1 + min2)
        return leftover_money if leftover_money >= 0 else money