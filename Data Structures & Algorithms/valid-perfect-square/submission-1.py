class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        odd_number = 1
        while num > 0:
            num -= odd_number
            odd_number += 2
        return num == 0