class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = r = 0

        while r < len(nums) - 1:
            next_r = 0
            for i in range(l, r + 1):
                next_r = max(next_r , i + nums[i])
            l = r + 1
            r = next_r
            jumps += 1
        return jumps
            
