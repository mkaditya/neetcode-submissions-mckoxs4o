class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def word_possibility():
            board_counts = Counter(char for row in board for char in row)
            word_counts = Counter(word)

            for char,count in word_counts.items():
                if board_counts[char] < count:
                    return False
            return True
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[i]:
                return False
            board[r][c] = '#'
            res = dfs(r+1, c , i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            board[r][c] = word[i]
            return res
        if not word_possibility():
            return False
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        
        return False