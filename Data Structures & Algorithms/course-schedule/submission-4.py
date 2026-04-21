class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = defaultdict(int)

        # (a, b) results in [b] --prereq for --> [a] graph

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        q = deque()
        for idx in range(numCourses):
            if indegree[idx] == 0:
                q.append(idx)

        completed_courses = 0
        while q:
            completable_course = q.popleft()
            completed_courses += 1
            dependent_courses = adj[completable_course]

            for dependent_course in dependent_courses:
                indegree[dependent_course] -= 1
                if indegree[dependent_course] == 0:
                    q.append(dependent_course)
        
        return completed_courses == numCourses
