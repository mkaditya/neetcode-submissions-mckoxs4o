class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num, idx) for idx, num in enumerate(nums)]
        heapq.heapify(heap)
        while k:
            num, idx = heapq.heappop(heap)
            heapq.heappush(heap, (num * multiplier, idx))
            k -= 1
        result = [0] * len(nums)
        for num, idx in heap:
            result[idx] = num
        return result