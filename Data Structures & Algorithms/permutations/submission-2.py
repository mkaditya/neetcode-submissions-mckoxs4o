class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # p(x) = x * p(x-1)
        if not nums:
            return [[]]
        
        res = []
        for idx in range(len(nums)):
            idx_res = [nums[idx]]
            for perm in self.permute(nums[:idx] + nums[idx+1:]):
                res.append(perm + idx_res)
        return res