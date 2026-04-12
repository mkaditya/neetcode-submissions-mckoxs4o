# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = float("-inf")
        self.max_sum(root)
        return self.result

    def max_sum(self, node):
        if not node:
            return 0
        
        left_max_sum = max(self.max_sum(node.left), 0)
        right_max_sum = max(self.max_sum(node.right), 0)
        curr_node_max_val = node.val + left_max_sum + right_max_sum
        self.result = max(self.result, curr_node_max_val)
        return node.val + max(left_max_sum, right_max_sum)