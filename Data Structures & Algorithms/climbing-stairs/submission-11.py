class Solution:
    def climbStairs(self, n: int) -> int:
        
        idx_minus_2, idx_minus_1 = 1, 1 # 0, 1

        for _ in range(n-1):
            idx_minus_1, idx_minus_2 = idx_minus_2 + idx_minus_1, idx_minus_1
        
        return idx_minus_1

