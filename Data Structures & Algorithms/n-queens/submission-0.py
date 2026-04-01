class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["." for _ in range(n)] for _ in range(n)]
        cols, positive_diag, negative_diag = set(),set(),set()

        def backtrack(row):
            if row == n:
                result.append([''.join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row-col) in negative_diag or (row+col) in positive_diag:
                    continue
                
                board[row][col] = 'Q'
                # mark visitied
                cols.add(col)
                negative_diag.add(row-col)
                positive_diag.add(row+col)

                backtrack(row+1)

                board[row][col] = '.'
                cols.remove(col)
                negative_diag.remove(row-col)
                positive_diag.remove(row+col)
        
        backtrack(0)
        return result