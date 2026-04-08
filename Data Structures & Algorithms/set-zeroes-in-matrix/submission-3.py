class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_len, col_len = len(matrix), len(matrix[0])
        
        row0_has_zero = any(matrix[0][c] == 0 for c in range(col_len))
        col0_has_zero = any(matrix[r][0] == 0 for r in range(row_len))

        for r_idx in range(1, row_len):
            for c_idx in range(1, col_len):
                if matrix[r_idx][c_idx] == 0:
                    matrix[r_idx][0] = 0 # flag the row
                    matrix[0][c_idx] = 0 # falg the col

        
        for r_idx in range(1, row_len):
            for c_idx in range(1, col_len):
                if matrix[r_idx][0] == 0 or matrix[0][c_idx] == 0:
                    matrix[r_idx][c_idx] = 0
        
        if row0_has_zero:
            for c_idx in range(col_len):
                matrix[0][c_idx] = 0
        
        if col0_has_zero:
            for r_idx in range(row_len):
                matrix[r_idx][0] = 0



        