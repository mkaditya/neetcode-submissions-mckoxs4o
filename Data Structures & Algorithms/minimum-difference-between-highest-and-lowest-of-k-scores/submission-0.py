class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_diff = float("inf")

        l, r = 0 , k -1
        while r < len(nums):
            min_diff = min(min_diff, nums[r] - nums[l])
            l += 1
            r += 1
        return min_diff



