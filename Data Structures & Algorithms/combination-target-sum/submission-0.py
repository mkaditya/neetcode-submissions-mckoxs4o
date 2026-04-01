class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, curr_list, curr_sum):
            if curr_sum == target:
                res.append(curr_list.copy())
                return

            if curr_sum > target or idx >= len(nums):
                return
            
            #number in idx included, we can use it unlimited no of times
            curr_list.append(nums[idx])
            dfs(idx, curr_list, curr_sum + nums[idx])
            # number in idx not included
            curr_list.pop() 
            dfs(idx+1, curr_list, curr_sum)
        
        dfs(0, [], 0)
        return res