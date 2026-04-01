class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r_size, c_size = len(matrix), len(matrix[0])
        t_size = r_size * c_size
        l, r = 0, t_size - 1

        while l <= r:
            m = (l + r) // 2
            r_idx = m // c_size
            c_idx = m % c_size
            curr_val = matrix[r_idx][c_idx]

            if curr_val == target:
                return True
            elif curr_val < target:
                l = m + 1
            else:
                r = m - 1
        return False
