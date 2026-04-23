class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list) # captures dependent courses
        indegree = defaultdict(int) # captures how many courses we are dependent on

        # a, b => b --is dependency of --> a
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegree[course] += 1

        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0: # i.e no prereq
                q.append(course)
        

        completed_courses = 0
        while q:
            course = q.popleft()
            completed_courses += 1

            dependent_courses = adj_list[course]
            for dep in dependent_courses:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    q.append(dep)
        
        return completed_courses == numCourses