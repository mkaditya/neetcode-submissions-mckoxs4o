class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        curr_sum = 0
        for idx, num in enumerate(nums):
            if nums[idx] <= nums[idx -1]:
                curr_sum = nums[idx]
            else:
                curr_sum += nums[idx]
            res = max(curr_sum, res)
        return res