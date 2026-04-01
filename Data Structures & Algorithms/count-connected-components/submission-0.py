class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [idx for idx in range(n)]

        def find(vertex):
            if parent[vertex] == vertex:
                return vertex
            return find(parent[vertex])
        
        total_components = n # everthing disconnected to begin with
        for edge in edges:
            parent_x = find(edge[0])
            parent_y = find(edge[1])
            if parent_x != parent_y: # merge them into one component
                parent[parent_x] = parent_y
                total_components -= 1
        
        return total_components
