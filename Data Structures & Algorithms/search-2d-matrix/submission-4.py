class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        l, r = 0, r * c - 1

        while l <= r:
            m = (l + r) // 2
            r_idx = m // c
            c_idx = m % c
            curr_val = matrix[r_idx][c_idx]
            if curr_val == target:
                return True
            elif curr_val < target:
                l = m + 1
            else:
                r = m - 1
        return False