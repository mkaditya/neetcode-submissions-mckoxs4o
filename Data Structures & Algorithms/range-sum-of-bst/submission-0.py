# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inorder(node, left_limit, right_limit) -> int:
            if not node:
                return 0
            if node.val < left_limit:
                return inorder(node.right, left_limit, right_limit)
            if node.val > right_limit:
                return inorder(node.left, left_limit, right_limit)
            return node.val + inorder(node.left, left_limit, right_limit) + inorder(node.right, left_limit, right_limit)
        return inorder(root, low, high)