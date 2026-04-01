class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda trip: trip[1])

        min_heap = [] # end, #of passengers
        curr_pass = 0

        for num_passengers, start, end in trips:
            # remove passengers whose trip has ended
            while min_heap and min_heap[0][0] <= start:
                curr_pass -= heapq.heappop(min_heap)[1]
            
            # add new passengers
            curr_pass += num_passengers

            # check capacity
            if curr_pass > capacity:
                return False

            # add this trip end time for further tracking
            heapq.heappush(min_heap, [end, num_passengers])
        return True
