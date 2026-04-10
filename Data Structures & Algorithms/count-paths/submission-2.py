class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.dp_memoization(m,n)

    # dp with memoization top-down
    def dp_memoization(self, m, n):
        cache = {}
        def dfs(x,y):
            if x == m - 1 and y == n - 1:
                return 1 # goal reached

            if x >= m or y >= n:
                return 0
            
            if (x,y) not in cache:
                cache[(x,y)] = dfs(x, y+1) + dfs(x+1, y)
            
            return cache[(x,y)]
        
        return dfs(0, 0)

    def dp_tabulation(self, m, n):
        # so that when we do i+1, j and i, j+1 it won't go out of bounds, addidtional row & col always have zero value
        dp = [[0] * (n+1) for _ in range(m+1)]

        # you are at end result, started there that is 1 one way to get there
        dp[m-1][n-1] = 1

        # now lets walk backwards, both in row & col manner while populating rest of entries.
        for r_idx in reversed(range(m)):
            for c_idx in reversed(range(n)):
                dp[r_idx][c_idx] = dp[r_idx + 1][c_idx] + dp[r_idx][c_idx+1]
        return dp[0][0]