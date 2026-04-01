class Solution:
    def findOrder(self, numCourses: int, prereqs: List[List[int]]) -> List[int]:
        graph = { vertex: [] for vertex in range(numCourses)}

        for dep in prereqs:
            graph[dep[0]].append(dep[1])
        
        visited = set()
        visiting = set()
        order = []

        def has_cycle(vertex):
            if vertex in visited:
                return False
            if vertex in visiting:
                return True
            
            visiting.add(vertex)
            for dep in graph[vertex]:
                if has_cycle(dep):
                    return True
            visiting.remove(vertex)
            visited.add(vertex)
            order.append(vertex)
            return False

        for vertex in range(numCourses):
            if has_cycle(vertex):
                return []
        
        return order


            
