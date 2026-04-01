class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        result = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            heapq.heappush_max(max_heap, (dist, x, y))
            if len(max_heap) > k:
                heapq.heappop_max(max_heap)
        
        for idx in range(len(max_heap)):
            dist, x, y = max_heap[idx]
            result.append([x, y])
        
        return result
