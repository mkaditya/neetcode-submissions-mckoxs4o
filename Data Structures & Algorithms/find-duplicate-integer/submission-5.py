class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        indexes = [1] * len(nums)

        for num in nums:
            num_idx = num - 1
            if indexes[num_idx] == -1:
                return num
            indexes[num_idx] = -1