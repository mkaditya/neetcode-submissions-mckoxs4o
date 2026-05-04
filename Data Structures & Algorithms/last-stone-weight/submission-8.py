class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return -1
        
        heapq._heapify_max(stones)

        while len(stones) > 1:
            y = heapq._heappop_max(stones)
            x = heapq._heappop_max(stones)
            if x != y:
                heapq._heappush_max(stones, y - x)
        
        return stones[0] if stones else 0