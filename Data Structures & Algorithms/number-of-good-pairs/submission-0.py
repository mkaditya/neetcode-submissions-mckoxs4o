class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = {}
        res = 0
        for x in nums:
            res += cnt.get(x, 0)
            cnt[x] = cnt.get(x, 0) + 1
        return res