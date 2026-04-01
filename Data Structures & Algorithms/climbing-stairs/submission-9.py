class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        idx_minus_1, idx_minus_2 = 2, 1

        for _ in range(3, n+1):
            idx_minus_1, idx_minus_2 = idx_minus_1 + idx_minus_2, idx_minus_1
        
        return idx_minus_1

