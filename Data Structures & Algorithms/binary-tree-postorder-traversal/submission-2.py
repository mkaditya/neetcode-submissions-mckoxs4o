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
        stack, result = [node], []
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        
        while result:
            self.result.append(result.pop())
