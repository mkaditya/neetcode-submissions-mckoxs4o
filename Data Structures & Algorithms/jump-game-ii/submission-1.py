class Solution:
    def jump(self, nums: List[int]) -> int: # [2,4,1,1,1,1]
        jumps = end = farthest = 0

        for idx in range(len(nums)-1):
            farthest = max(farthest, idx + nums[idx])
            if idx == end:
                jumps += 1
                end = farthest
        
        return jumps
