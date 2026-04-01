class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in cnt.items():
            buckets[freq].append(num)
        
        result = []
        for b in buckets[::-1]:
            for n in b:
                result.append(n)
                if len(result) == k:
                    return result
        return result
