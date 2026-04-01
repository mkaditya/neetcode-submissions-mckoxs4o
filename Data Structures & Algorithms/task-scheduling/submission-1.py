class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = []
        for val in count.values():
            heapq.heappush_max(max_heap, val)

        cooldown_q = deque()
        time = 0

        while max_heap or cooldown_q:
            time += 1
            if max_heap:
                cnt = heapq.heappop_max(max_heap) - 1
                if cnt > 0:
                    cooldown_q.append([cnt, time + n])
            else:
                time = cooldown_q[0][1]

            if cooldown_q and cooldown_q[0][1] == time:
                heapq.heappush_max(max_heap, cooldown_q.popleft()[0])

        return time