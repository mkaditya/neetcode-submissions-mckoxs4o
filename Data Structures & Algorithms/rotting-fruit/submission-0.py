class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY_CELL, FRESH_FRUIT, ROTTEN_FRUIT = 0, 1, 2
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[1,0], [-1,0], [0,1], [0, -1]]

        rotten_fruits = deque()
        visited = set()
        min_minutes = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == ROTTEN_FRUIT:
                    rotten_fruits.append((r,c))
                    visited.add((r,c))
        
        while rotten_fruits:
            for _ in range(len(rotten_fruits)):
                (r, c) = rotten_fruits.popleft()
                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if (0 <= nr < ROWS and 
                        0 <= nc < COLS and 
                        grid[nr][nc] == FRESH_FRUIT and 
                        (nr, nc) not in visited):
                        rotten_fruits.append((nr, nc))
                        grid[nr][nc] = ROTTEN_FRUIT

            if rotten_fruits:
                min_minutes += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == FRESH_FRUIT:
                    return -1
        return min_minutes
            


