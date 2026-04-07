# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.dfs_r(root)
        return self.result

    def dfs_r(self, node):
        if not node:
            return
        self.dfs_r(node.left)
        self.dfs_r(node.right)
        self.result.append(node.val)