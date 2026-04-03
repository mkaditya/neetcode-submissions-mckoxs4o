class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        1 = 1²
        1 + 3 = 4 = 2²
        1 + 3 + 5 = 9 = 3²
        1 + 3 + 5 + 7 = 16 = 4²
        """
        odd_number = 1
        while num > 0:
            num -= odd_number
            odd_number += 2
        return num == 0