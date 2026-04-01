class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}

        def find_parent(vertex):
            if vertex not in parent:
                parent[vertex] = vertex
            if parent[vertex] != vertex:
                parent[vertex] = find_parent(parent[vertex])
            return parent[vertex]

        def union(x, y):
            px, py = find_parent(x), find_parent(y)
            if px == py:
                return False
            
            parent[px] = py
            return True
        

        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge
        return []
            