class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = { vertex: [] for vertex in range(numCourses)}

        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])
        
        fully_explored = set()
        visiting = set()

        def has_cycle(course):
            if course in fully_explored:
                return False
            if course in visiting:
                return True

            visiting.add(course)
            for prereq in graph[course]:
                if has_cycle(prereq):
                    return True
            visiting.remove(course)
            fully_explored.add(course)
            return False
        
        for course in range(numCourses):
            if has_cycle(course):
                return False
        return True