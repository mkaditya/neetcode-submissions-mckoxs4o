class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [cnt for cnt in count.values()]
        heapq.heapify_max(max_heap)

        time = 0
        q = deque()

        while max_heap or q:
            time += 1
            if not max_heap:
                time = q[0][1]
            else:
                cnt = heapq.heappop_max(max_heap) - 1
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush_max(max_heap, q.popleft()[0])
        return time