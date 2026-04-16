class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        cache = {}
        def dfs(idx, curr_target):
            if curr_target == 0:# found a valid subset
                return True
            if idx >= len(nums) or curr_target < 0: 
                return False
            if (idx, curr_target) in cache:
                return cache[(idx, curr_target)]
            cache[(idx, curr_target)] = dfs(idx + 1, curr_target) or dfs(idx+1, curr_target - nums[idx])
            return cache[(idx, curr_target)]
        
        return dfs(0, target)