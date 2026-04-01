class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = { vertex: [] for vertex in range(numCourses)}

        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])
        
        completable_courses = set()
        dependent_courses = set()

        def has_cycle(course):
            if course in completable_courses:
                return False
            if course in dependent_courses:
                return True

            dependent_courses.add(course)
            for prereq in graph[course]:
                if has_cycle(prereq):
                    return True
            dependent_courses.remove(course)
            completable_courses.add(course)
            return False
        
        for course in range(numCourses):
            if has_cycle(course):
                return False
        return True