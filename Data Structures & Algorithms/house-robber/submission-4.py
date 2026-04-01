class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        nums_minus_2 = nums[0]
        nums_minus_1 = max(nums[0],  nums[1])

        for idx in range(2, len(nums)):
            curr_max = max(nums_minus_1 , nums[idx] + nums_minus_2)
            nums_minus_2 = nums_minus_1
            nums_minus_1 = curr_max
        return nums_minus_1