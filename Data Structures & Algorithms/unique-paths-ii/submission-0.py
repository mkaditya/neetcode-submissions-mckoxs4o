class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])
    
        # Initialize DP matrix with R+1 rows and C+1 columns, all zeros
        # dp[i][j] will represent the number of ways to reach cell (i-1, j-1)
        dp = [[0] * (C + 1) for _ in range(R + 1)]

        if obstacleGrid[R-1][C-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        dp[R-1][C-1] = 1 # reached the target

        for r_idx in reversed(range(R)):
            for c_idx in reversed(range(C)):
                if r_idx == R-1 and c_idx == C-1:
                    continue
                
                if obstacleGrid[r_idx][c_idx] == 1:
                    dp[r_idx][c_idx] = 0
                else:
                    row_tracking, col_tracking = 0, 0
                    if r_idx + 1 < R:
                        row_tracking = dp[r_idx + 1][c_idx]
                    if c_idx + 1 < C:
                        col_tracking = dp[r_idx][c_idx+1]
                    dp[r_idx][c_idx] = row_tracking + col_tracking
        return dp[0][0]