class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        timeslots = [s for s in slots1 + slots2 if s[1] - s[0] >= duration]
        heapq.heapify(timeslots)

        while len(timeslots) > 1:
            start, end = heapq.heappop(timeslots)
            next_start, next_end = heapq.heappop(timeslots)
            if end >= next_start + duration:
                return [next_start, next_start + duration]
            else:
                heapq.heappush(timeslots, [next_start, next_end])
        return []