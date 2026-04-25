class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = defaultdict(list)
        indegree = defaultdict(int)
        prereq_map = defaultdict(set)

        for prereq, course in prerequisites:
            adj_list[prereq].append(course)
            indegree[course] += 1

        q = deque([idx for idx in range(numCourses) if indegree[idx] == 0])
        
        while q:
            course = q.popleft()
            for dep in adj_list[course]:
                prereq_map[dep].add(course)
                prereq_map[dep].update(prereq_map[course])
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    q.append(dep)
        
        res = []
        for prereq, course in queries:
            res.append(prereq in prereq_map[course])
        return res