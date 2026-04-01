class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for idx, jump_length in enumerate(nums):
            if idx > farthest: 
                return False
            farthest = max(farthest, idx + jump_length)
        return True