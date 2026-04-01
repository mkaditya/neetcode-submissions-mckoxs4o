class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = r  = 0
        next_right = 0
        while l <= r and r < len(nums):
            for i in range(l, r+1):
                next_right = max(next_right, nums[i] + i)
            l, r = r + 1, next_right

        return r >= len(nums) - 1