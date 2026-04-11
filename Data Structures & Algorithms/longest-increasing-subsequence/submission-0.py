class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 1
        return self.n2_solution(nums)

    def n2_solution(self, nums):
        dp = [1] * len(nums)
        for idx in range(1, len(nums)):
            possible_lis = [dp[i] for i in range(idx) if nums[i] < nums[idx]]
            if possible_lis:
                dp[idx] = 1 + max(possible_lis)
        
        return max(dp)
        