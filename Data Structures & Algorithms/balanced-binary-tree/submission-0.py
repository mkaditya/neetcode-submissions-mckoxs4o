# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.check_balance(root)[0]

    def check_balance(self, root: Optional[TreeNode]) -> tuple[bool, int]:
        if not root:
            return True, 0
        
        left_balance, left_height = self.check_balance(root.left)
        right_balance, right_height = self.check_balance(root.right)
        is_balanced = left_balance and right_balance and abs(left_height - right_height) <= 1
        return is_balanced, 1 + max(left_height, right_height)
