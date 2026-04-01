class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                curr_val = board[r][c]
                if (curr_val in rows[r] or 
                    curr_val in cols[c] or 
                    curr_val in squares[(r//3, c//3)]):
                    return False
                cols[c].add(curr_val)
                rows[r].add(curr_val)
                squares[(r//3, c//3)].add(curr_val)
        return True