class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(idx):
            if idx == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[idx]) # include current number
            backtrack(idx + 1)

            subset.pop()  # don't include current number
            backtrack(idx + 1) 

        backtrack(0)
        return res