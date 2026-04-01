class Solution:
    def __construct_graph(self, graph, prereqs):
        for main, dep_course in prereqs:
            graph[main].append(dep_course)

    def __has_cycle(self, graph, course, visiting, fully_explored):
        if course in fully_explored:
            return False
        if course in visiting:
            return True

        visiting.add(course)
        for dep_course in graph[course]:
            if self.__has_cycle(graph, dep_course, visiting, fully_explored):
                return True
        
        visiting.remove(course)
        fully_explored.add(course)
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = { vertex: [] for vertex in range(numCourses)}
        self.__construct_graph(graph, prerequisites)

        fully_explored = set()
        visiting = set()

        
        for course in range(numCourses):
            if self.__has_cycle(graph, course, fully_explored,visiting):
                return False
        return True