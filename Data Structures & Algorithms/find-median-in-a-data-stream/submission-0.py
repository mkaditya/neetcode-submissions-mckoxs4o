class MedianFinder:

    def __init__(self):
        # max_heap stores smaller half, min_heap stores larger half
        self.max_heap, self.min_heap = [], []        

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush_max(self.max_heap, num)
        
        # Balance the heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = heapq.heappop_max(self.max_heap)
            heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > len(self.max_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush_max(self.max_heap, val)

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]
        return (self.min_heap[0] + self.max_heap[0])/2.0
        
        