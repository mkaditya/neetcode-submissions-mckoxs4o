class Solution:
    def rob(self, nums: List[int]) -> int:
        idx_minus_1 = 0
        idx_minus_2 = 0

        for idx, num in enumerate(nums):
            curr_max = max(num + idx_minus_2 , idx_minus_1)
            idx_minus_2 = idx_minus_1
            idx_minus_1 = curr_max
        
        return idx_minus_1

            