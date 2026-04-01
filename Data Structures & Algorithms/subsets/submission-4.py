class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        for eval_number in range(1<<n):
            subset = [nums[i] for i in range(n) if eval_number & (1<<i)]
            res.append(subset)
        return res
