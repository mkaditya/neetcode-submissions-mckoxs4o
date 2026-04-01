class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return nums[0]
        
        def rob_linear(houses):
            house_minus_2, house_minus_1 = 0, 0
            for house in houses:
                curr_max = max(house_minus_1, house + house_minus_2)
                house_minus_2 = house_minus_1
                house_minus_1 = curr_max
            return house_minus_1
        
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))