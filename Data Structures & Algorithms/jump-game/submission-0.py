class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = r = 0
        
        while r < len(nums) - 1 and l <= r:
            next_r = 0
            for i in range(l, r+1):
                next_r = max(next_r, i + nums[i])
            l = r + 1
            r = next_r
        
        return r >= len(nums) - 1
