class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l_idx = 1
        for r_idx in range(1, len(nums)):
            if nums[r_idx] != nums[r_idx-1]:
                nums[l_idx] = nums[r_idx]
                l_idx += 1
        return l_idx