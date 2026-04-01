class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if not nums:
            return 0

        def kadane_max() -> int:
            max_sum = nums[0]
            curr_sum = 0

            for num in nums:
                curr_sum = max(curr_sum + num , num)
                max_sum = max(max_sum, curr_sum)

            return max_sum

        def kadane_min() -> int:
            min_sum = nums[0]
            curr_sum = 0

            for num in nums:
                curr_sum = min(curr_sum + num, num)
                min_sum = min(min_sum, curr_sum)
            return min_sum

        kadane_max, kadane_min = kadane_max(), kadane_min()
        wrap = sum(nums) - kadane_min
        return max(kadane_max,  kadane_max if wrap == 0 else wrap)

        
