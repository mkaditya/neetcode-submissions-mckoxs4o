class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.squared_number(n)

            if n == 1:
                return True
            
            if n in visited:
                return False

    def squared_number(self, n: int) -> int:
        curr_sum = 0

        while n:
            remainder = n % 10
            curr_sum += remainder * remainder
            n = n // 10
        return curr_sum
        