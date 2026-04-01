class Solution:
    def climbStairs(self, n: int) -> int:
        
        idx, idx_minus_1 = 1, 1

        for _ in range(n-1):
            idx, idx_minus_1 = idx + idx_minus_1, idx
        
        return idx

