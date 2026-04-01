class Solution:
    def rob(self, nums: List[int]) -> int:
        nums_minus_2, nums_minus_1 = 0, 0
        for num in nums:
            curr_max = max(nums_minus_1, num + nums_minus_2)
            nums_minus_2 = nums_minus_1
            nums_minus_1 = curr_max
        return nums_minus_1