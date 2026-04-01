class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        rob_value = [0] * len(nums)
        rob_value[0] = nums[0]
        rob_value[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            rob_value[i] = max(rob_value[i - 1], nums[i] + rob_value[i-2])
        
        return rob_value[len(nums) - 1]