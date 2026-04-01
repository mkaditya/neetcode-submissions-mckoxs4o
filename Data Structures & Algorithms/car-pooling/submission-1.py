class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda trip:trip[1])
        min_heap = []
        curr_passengers = 0

        for num_passengers, start_time, end_time in trips:
            # before this trip, passengers are getting dropped off
            while min_heap and min_heap[0][0] <= start_time:
                curr_passengers -= heapq.heappop(min_heap)[1]
            
            curr_passengers += num_passengers
            if curr_passengers > capacity: # overloaded
                return False
            heapq.heappush(min_heap, [end_time, num_passengers]) # new passengers in car
        return True
