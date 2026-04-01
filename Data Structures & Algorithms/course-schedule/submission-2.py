class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = { vertex:[] for vertex in range(numCourses)}

        for main, dep_course in prerequisites:
            graph[main].append(dep_course)

        fully_explored = set()
        visiting = set()

        def has_cycle(course):
            if course in fully_explored:
                return False
            if course in visiting:
                return True

            visiting.add(course)
            for dep_course in graph[course]:
                if has_cycle(dep_course):
                    return True
            
            visiting.remove(course)
            fully_explored.add(course)
            return False

        
        for course in range(numCourses):
            if has_cycle(course):
                return False
        return True