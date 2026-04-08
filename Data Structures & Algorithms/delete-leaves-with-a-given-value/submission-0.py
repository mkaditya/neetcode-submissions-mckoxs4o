# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        return self.removeLeaves(root, target)
    

    def removeLeaves(self, node, target):
        if node is None:
            return None
        
        node.left = self.removeLeaves(node.left, target)
        node.right = self.removeLeaves(node.right, target)

        if node.left is None and node.right is None and node.val == target:
            return None
        
        return node
