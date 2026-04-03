# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.preorder_iter(root)
        return self.result

    def preorder(self, node):
        if not node:
            return 
        self.result.append(node.val)
        self.preorder(node.left)
        self.preorder(node.right)

    def preorder_iter(self, node):
        if not node:
            return
        
        stack = [node]
        # do inverser processing of recursive as stack is LIFO and recurison is LIFO
        while stack:
            node = stack.pop()
            self.result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
