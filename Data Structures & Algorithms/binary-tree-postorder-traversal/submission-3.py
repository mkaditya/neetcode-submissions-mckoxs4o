# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.dfs_i(root)
        return self.result

    def dfs_r(self, node):
        if not node:
            return
        self.dfs_r(node.left)
        self.dfs_r(node.right)
        self.result.append(node.val)
    
    def dfs_i(self, node):
        if not node:
            return
        stack = [(node, False)]

        while stack:
            curr, visited = stack.pop()
            if visited:
                self.result.append(curr.val)
            else:
                stack.append((curr, True))
                if curr.right:
                    stack.append((curr.right, False))
                if curr.left:
                    stack.append((curr.left, False))
