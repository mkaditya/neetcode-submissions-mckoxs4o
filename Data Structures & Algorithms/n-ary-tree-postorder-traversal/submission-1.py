"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.result = []
        self.dfs_r(root)
        return self.result
    
    def dfs_r(self, node):
        if not node:
            return
        
        if node.children:
            for child in node.children:
                self.dfs_r(child)
        
        self.result.append(node.val)

    def dfs_i(self, node):
        stack = [(node, False)]
        while stack:
            node, visited = stack.pop()
            if visited:
                self.result.append(node.val)
            else:
                stack.append((node, True))
                for child in reversed(node.children):
                    stack.append((child, False))

