# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if not subRoot:
            return True

        if not root:
            return False

        if self.is_same_tree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def is_same_tree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        
        if not root1 or not root2 or root1.val != root2.val:
            return False
        
        return self.is_same_tree(root1.left, root2.left) and self.is_same_tree(root2.right, root1.right)