class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        water, treasure = -1, 0
        visited = set()
        q = deque()
        r_count, c_count = len(grid), len(grid[0])

        for r_idx in range(r_count):
            for c_idx in range(c_count):
                if grid[r_idx][c_idx] == treasure:
                    visited.add((r_idx, c_idx))
                    q.append((r_idx, c_idx))
        
        distance = 0
        while q:
            for _ in range(len(q)):
                (r_idx, c_idx) = q.popleft()
                grid[r_idx][c_idx] = distance

                directions = [
                    (r_idx + 1, c_idx), 
                    (r_idx - 1, c_idx),
                    (r_idx, c_idx + 1),
                    (r_idx, c_idx - 1)
                ]
                
                for nr, nc in directions:
                    if ( 
                        0 <= nr < r_count and 0 <= nc < c_count 
                        and (nr, nc) not in visited 
                        and grid[nr][nc] != treasure
                        and grid[nr][nc] != water
                    ):
                        q.append((nr, nc))
                        visited.add((nr, nc))
            distance += 1

            
        
        