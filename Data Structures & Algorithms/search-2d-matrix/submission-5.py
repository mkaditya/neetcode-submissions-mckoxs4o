class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, (rows * cols) - 1

        while l <= r:
            m = (l + r) // 2
            r_idx, c_idx = m // cols, m % cols
            if matrix[r_idx][c_idx] == target:
                return True
            elif matrix[r_idx][c_idx] < target:
                l = m + 1
            else:
                r = m - 1
        return False
