class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count freq of each num
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq = [[] for _ in range(len(nums))]

        for num, cnt in count.items():
            freq[cnt-1].append(num)

        res = []
        for i in reversed(range(len(freq))):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res