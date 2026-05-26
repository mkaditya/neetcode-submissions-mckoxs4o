class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        indegree = defaultdict(int)

        for dep_course, course in prerequisites:
            adj_list[course].append(dep_course)
            indegree[dep_course] += 1
        
        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        completed_courses = 0
        while q:
            q_len = len(q)
            for _ in range(q_len):
                course = q.popleft()
                completed_courses += 1
                for dep_course in adj_list[course]:
                    indegree[dep_course] -= 1
                    if indegree[dep_course] == 0:
                        q.append(dep_course)
        
        return completed_courses == numCourses