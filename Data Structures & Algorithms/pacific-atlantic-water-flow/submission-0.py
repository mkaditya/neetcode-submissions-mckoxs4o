class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visited):
            visited.add((r,c))
            for dr,dc in [(0,1), (0,-1), (1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < ROWS and 
                    0 <= nc < COLS and 
                    (nr,nc) not in visited 
                    and heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr,nc,visited)

        for c in range(COLS):
            dfs(0, c, pacific)
            dfs(ROWS-1, c, atlantic)

        for r in range(ROWS):
            dfs(r, 0, pacific)
            dfs(r, COLS-1, atlantic)
        
        return list(pacific & atlantic)