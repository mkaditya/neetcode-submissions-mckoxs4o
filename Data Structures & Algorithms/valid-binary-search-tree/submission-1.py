# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid(root, float("-inf"), float("inf"))
    
    def is_valid(self, node, min_val, max_val):
        if not node:
            return True

        if min_val < node.val < max_val:
            return self.is_valid(node.left, min_val, node.val) and self.is_valid(node.right, node.val, max_val)
        else:
            return False