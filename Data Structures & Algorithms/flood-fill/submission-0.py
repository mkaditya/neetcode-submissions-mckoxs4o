class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # no work
        if image[sr][sc] == color:
            return image

        self.dfs(image, sr, sc, image[sr][sc], color)
        return image

    
    def dfs(self, image, i, j, sr_color, dt_color):
        if i < 0 or i >= len(image) or j < 0 or j >= len(image[i]) or image[i][j] != sr_color:
            return
        
        image[i][j] = dt_color
        self.dfs(image, i+1, j, sr_color, dt_color)
        self.dfs(image, i, j+1, sr_color, dt_color)
        self.dfs(image, i-1, j, sr_color, dt_color)
        self.dfs(image, i, j-1, sr_color, dt_color)