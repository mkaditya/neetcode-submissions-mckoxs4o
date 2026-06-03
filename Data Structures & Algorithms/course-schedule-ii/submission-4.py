class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = defaultdict(int)
        res = []

        for course, dep_course in prerequisites:
            adj_list[dep_course].append(course)
            indegree[course] += 1
        
        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        while q:
            course = q.popleft()
            res.append(course)

            deps = adj_list[course]
            for dep in deps:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    q.append(dep)
        
        return [] if len(res) != numCourses else res
            
