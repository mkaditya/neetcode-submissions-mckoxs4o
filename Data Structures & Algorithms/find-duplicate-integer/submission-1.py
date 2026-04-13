class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            num_idx = abs(num) - 1
            if nums[num_idx] < 0:
                return abs(num) # this number is already visistied
            # mark visit
            nums[num_idx] *= -1
        return -1