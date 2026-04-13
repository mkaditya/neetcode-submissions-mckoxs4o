# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # return self.depth_iter(root)
        return self.practice(root)


    def practice(self, node):
        if not node:
            return 0
        return 1 + max(self.practice(node.left), self.practice(node.right))

    
    def depth(self, node):
        if not node:
            return 0
        return 1 + max(self.depth(node.left), self.depth(node.right))
    
    def depth_iter(self, node):
        if not node:
            return 0
        stack = [(node, 1)]
        result = 0
        while stack:
            n, d = stack.pop()
            if n.left:
                stack.append((n.left, d + 1))
            if n.right:
                stack.append((n.right, d + 1))
            result = max(result, d)
        return result
