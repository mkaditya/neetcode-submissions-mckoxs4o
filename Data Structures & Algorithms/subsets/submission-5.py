class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        for i in range(1 << n):
            res.append([nums[j] for j in range(n) if i & (1<<j)])
        return res