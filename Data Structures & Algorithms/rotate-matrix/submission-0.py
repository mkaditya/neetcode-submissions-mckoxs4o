class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Start:       [i][j]
        Transpose:   [j][i]          (swap indices)
        Reverse row: [j][n-1-i]      (i becomes n-1-i, j stays as row)
        """
        R = len(matrix) # row and col length would be same since it is square
        """
        i=0:  . X X
        i=1:  . . X
        i=2:  . . . 
        """
        # transpose, since we are doing non diagonal swap, rows & columsn are swapped.
        for i in range(R):
            for j in range(i + 1, R):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for row in matrix:
            row.reverse()