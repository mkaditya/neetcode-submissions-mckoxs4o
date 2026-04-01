class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        idx_tasks = [(tasks[idx][0], tasks[idx][1], idx) for idx in range(n)]
        idx_tasks.sort() # do sorting by ready time

        min_heap = [] # order of tasks
        c_idx = 0 # current idx
        res = []
        time = 0

        while min_heap or c_idx < n:
            while c_idx < n and idx_tasks[c_idx][0] <= time:
                heapq.heappush(min_heap, (idx_tasks[c_idx][1], idx_tasks[c_idx][2]))
                c_idx += 1
            
            if not min_heap:
                time = idx_tasks[c_idx][0]
            else:
                processing_time, idx = heapq.heappop(min_heap)
                time += processing_time
                res.append(idx)
        return res