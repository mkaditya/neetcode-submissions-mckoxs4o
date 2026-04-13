# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # self.mirror_iterative(root)
        self.practice(root)
        return root
    
    def practice(self, node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        self.practice(node.left)
        self.practice(node.right)

    def mirror(self, node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        self.mirror(node.left)
        self.mirror(node.right)

    def mirror_iterative(self, node):
        if not node:
            return
        
        stack = [node]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return
        