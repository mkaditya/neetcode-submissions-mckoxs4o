class Matrix:

    def __init__(self, grid: List[List[str]]):
        self.grid = grid
        self.row_len, self.col_len = len(grid), len(grid[0])
        self.visited = set()
    
    def get_island_count(self) -> int:
        island_count = 0
        for r_idx in range(self.row_len):
            for c_idx in range(self.col_len):
                if self.grid[r_idx][c_idx] == "1" and (r_idx, c_idx) not in self.visited:
                    self.dfs(r_idx, c_idx)
                    island_count += 1
        
        return island_count

    def dfs(self, r_idx: int, c_idx:int) -> None:
        if (
            r_idx < 0 or r_idx >= self.row_len or
            c_idx < 0 or c_idx >= self.col_len or
            self.grid[r_idx][c_idx] == "0" or
            (r_idx, c_idx) in self.visited
        ):
            return
        
        self.visited.add((r_idx, c_idx))
        for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            self.dfs(r_idx + dr, c_idx + dc)



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return Matrix(grid).get_island_count()
        