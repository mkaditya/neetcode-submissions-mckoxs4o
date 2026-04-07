class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p = 1
        min_p = 1
        res = nums[0]

        for num in nums:
            curr_max_p = max_p * num
            curr_min_p = min_p * num
            max_p = max(curr_max_p, curr_min_p, num)
            min_p = min(curr_max_p, curr_min_p, num)
            res = max(res, max_p)

        return max(max_p, res)