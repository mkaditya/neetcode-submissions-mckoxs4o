class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        cols, positive_diag, negative_diag = set(),set(),set()
        board = [["." for _ in range(n)] for _ in range(n)]

        def place_queen(row_idx):
            if row_idx == n:
                result.append(["".join(row) for row in board])
                return

            for col_idx in range(n):
                if col_idx in cols or row_idx+col_idx in positive_diag or row_idx-col_idx in negative_diag:
                    continue
                
                cols.add(col_idx), positive_diag.add(row_idx+col_idx), negative_diag.add(row_idx-col_idx)
                board[row_idx][col_idx] = "Q"
                place_queen(row_idx+1)
                board[row_idx][col_idx] = "."
                cols.remove(col_idx), positive_diag.remove(row_idx+col_idx), negative_diag.remove(row_idx-col_idx)

        place_queen(0)
        return result