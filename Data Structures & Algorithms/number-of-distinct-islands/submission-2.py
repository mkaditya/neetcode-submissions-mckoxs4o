class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        result = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    result.add(self.island(grid, i, j, "S"))
        return len(result)

    def island(self, grid, i, j, direction):
        if i < 0 or i >= len(grid) or j < 0 or j >=len(grid[i]) or grid[i][j] != 1:
            return ""
        
        grid[i][j] = -1
        direction += self.island(grid, i+1, j, "D")
        direction += self.island(grid, i, j+1, "R")
        direction += self.island(grid, i, j-1, "L")
        direction += self.island(grid, i-1, j, "U")
        direction += "E"
        return direction




