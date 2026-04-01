class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)

        while k:
            curr_val = heapq.heappop_max(gifts)
            heapq.heappush_max(gifts, int(sqrt(curr_val)))
            k = k - 1
        return sum(gifts)