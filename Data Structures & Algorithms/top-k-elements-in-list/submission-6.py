class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1
        
        for key, val in count.items():
            freq[val].append(key)

        res = []
        for idx in reversed(range(len(nums) + 1)):
            for num in freq[idx]:
                res.append(num)
                if len(res) == k:
                    return res
        return res