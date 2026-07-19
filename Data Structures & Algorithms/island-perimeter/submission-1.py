class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n, res = len(grid), len(grid[0]), 0
        visit = set()

        def dfs(i,j):
            if i < 0 or j < 0 or i >= m or j >=n or grid[i][j] == 0:
                return 1
            if (i, j) in visit:
                return 0
            visit.add((i,j))
            perim = dfs(i, j + 1) + dfs(i, j-1) + dfs(i+1, j) + dfs(i-1, j)
            return perim
            
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += dfs(i, j)
                    # res += (i+1 >= m or grid[i+1][j] == 0)
                    # res += (i-1 < 0 or grid[i-1][j] == 0)
                    # res += (j+1 >= n or grid[i][j+1] == 0)
                    # res += (j-1 < 0 or grid[i][j-1] == 0)
        return res