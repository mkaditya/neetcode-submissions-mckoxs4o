class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_len, col_len = len(matrix), len(matrix[0])
        
        rowZero = False

        for r_idx in range(row_len):
            for c_idx in range(col_len):
                if matrix[r_idx][c_idx] == 0:
                    # mark first row & col for zero flagging
                    if r_idx == 0: # we are using cols to mark
                        rowZero = True
                    else:
                        matrix[r_idx][0] = 0
                    matrix[0][c_idx] = 0
        
        for r_idx in range(1, row_len):
            for c_idx in range(1, col_len):
                if matrix[r_idx][0] == 0 or matrix[0][c_idx] == 0:
                    matrix[r_idx][c_idx] = 0
        
        if matrix[0][0] == 0:
            for r_idx in range(row_len):
                matrix[r_idx][0] = 0
        
        if rowZero:
            for c_idx in range(col_len):
                matrix[0][c_idx] = 0

        