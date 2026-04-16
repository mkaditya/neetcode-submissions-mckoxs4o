class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        result = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    result.add(self.island(grid, i, j))
        return len(result)

    def island(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >=len(grid[i]) or grid[i][j] != 1:
            return ""
        
        result = ""
        grid[i][j] = -1
        result += "D" + self.island(grid, i+1, j)
        result += "R" + self.island(grid, i, j+1)
        result += "L" + self.island(grid, i, j-1)
        result += "U" + self.island(grid, i-1, j)
        return result




