class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        parent = [idx for idx in range(n)]

        def find_parent(vertex):
            if parent[vertex] == vertex:
                return vertex
            return find_parent(parent[vertex])

        for edge in edges:
            parent_x = find_parent(edge[0])
            parent_y = find_parent(edge[1])
            if parent_x == parent_y:
                return False
            parent[parent_x] = parent_y
        
        return True
        

