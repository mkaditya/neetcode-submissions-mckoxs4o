class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        num_of_islands = 0
        visited = set()

        def dfs(r,c):
            if not 0 <= r < ROWS or not 0 <= c < COLS or (r,c) in visited:
                return
            
            visited.add((r,c))
            if grid[r][c] == "1":
                grid[r][c] = "2"
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    num_of_islands += 1
                    dfs(r, c)
        return num_of_islands
