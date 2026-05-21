class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l_idx = 0
        for r_idx in range(len(nums)):
            if nums[r_idx]:
                nums[l_idx], nums[r_idx] = nums[r_idx], nums[l_idx]
                l_idx += 1
        