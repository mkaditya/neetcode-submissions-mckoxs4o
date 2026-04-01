class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        boxs = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                curr_val = board[r][c]
                if curr_val == ".":
                    continue
                idx =  (r//3 , c//3)
                if curr_val in rows[r] or curr_val in cols[c] or curr_val in boxs[idx]:
                    return False
                cols[c].add(curr_val)
                rows[r].add(curr_val)
                boxs[idx].add(curr_val)
        return True

