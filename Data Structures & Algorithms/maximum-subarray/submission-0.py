class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = float("-inf")
        curr_sum = 0

        for num in nums:
            curr_sum = num + max(0, curr_sum)
            max_so_far = max(max_so_far, curr_sum)
        return max_so_far