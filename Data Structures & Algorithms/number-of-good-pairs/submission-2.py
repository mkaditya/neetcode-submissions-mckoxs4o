class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        res = 0
        for x in nums:
            res += cnt[x]
            cnt[x] += 1
        return res