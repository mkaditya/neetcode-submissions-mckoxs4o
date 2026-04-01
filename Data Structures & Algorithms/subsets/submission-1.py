class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(idx, path):
            if idx == len(nums):
                res.append(path)
                return
            
            backtrack(idx + 1, path + [nums[idx]]) # include current number
            backtrack(idx + 1, path) # don't include current number

        backtrack(0, [])
        return res