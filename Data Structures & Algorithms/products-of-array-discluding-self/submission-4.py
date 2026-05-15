class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for idx in range(len(nums)):
            res[idx] = prefix
            prefix = prefix * nums[idx]
        
        suffix = 1
        for idx in reversed(range(len(nums))):
            res[idx] *= suffix
            suffix = suffix * nums[idx]
        return res