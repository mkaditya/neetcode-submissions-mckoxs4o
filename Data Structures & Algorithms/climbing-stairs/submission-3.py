class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2: return n
        dp = [None] * (n+1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] # at 'n' steps you can take either 1 or 2 steps. Total ways is n-1 + n-2 problem
        return dp[n]