class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp with memoization top-down
        return self.dp_memoization(m,n)

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
