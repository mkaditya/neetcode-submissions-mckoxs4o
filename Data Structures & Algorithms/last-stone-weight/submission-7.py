class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]

        heapq.heapify_max(stones)

        while len(stones) >= 2:
            first_stone = heapq.heappop_max(stones)
            second_stone = heapq.heappop_max(stones)
            new_stone = first_stone - second_stone
            if new_stone != 0:
                heapq.heappush_max(stones, new_stone)
        
        return stones[0] if stones else 0
