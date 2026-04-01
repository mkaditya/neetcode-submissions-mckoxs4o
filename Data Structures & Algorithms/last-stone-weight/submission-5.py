class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            if stone1 == stone2:
                continue
            heapq.heappush_max(stones, stone1 - stone2)
        return 0 if not stones else heapq.heappop_max(stones)
