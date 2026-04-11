class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 1
        return self.n2_solution(nums)

    def n2_solution(self, nums):
        dp = [1] * len(nums)
        for idx in range(1, len(nums)):
           for solved_idx in range(idx):
            if nums[solved_idx] < nums[idx]:
                dp[idx] = max(1 + dp[solved_idx], dp[idx])
        
        return max(dp)
        