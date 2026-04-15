class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {idx: [] for idx in range(1, n+1)}
        in_count = {idx: 0 for idx in range(1, n+1)}

        for start_node, end_node in relations:
            graph[start_node].append(end_node)
            in_count[end_node] += 1

        q = deque()

        for idx in graph:
            if in_count[idx] == 0:
                q.append(idx)
        
        step = 0
        completed = 0

        while q:
            step += 1
            q_len = len(q)
            for _ in range(q_len):
                completed += 1
                idx = q.popleft()
                end_nodes = graph[idx]
                for end_node in end_nodes:
                    in_count[end_node] -= 1
                    if in_count[end_node] == 0:
                        q.append(end_node)
        
        return step if completed == n else -1



