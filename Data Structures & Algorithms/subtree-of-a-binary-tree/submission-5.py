# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # return self.sub_tree(root, subRoot)
        return self.practice(root, subRoot)

    def practice(self, root, sub_root):
        if root is None and sub_root is not None:
            return False
        if root is None and sub_root is None:
            return True
        
        if root.val == sub_root.val and self.is_same(root, sub_root):
            return True
        else:
            return self.practice(root.left, sub_root) or self.practice(root.right, sub_root)


    def is_same(self, root, sub_root):
        if root is None and sub_root is None:
            return True
        
        if root and sub_root and root.val == sub_root.val:
            return self.is_same(root.left, sub_root.left) and self.is_same(root.right, sub_root.right)
    
    def sub_tree(self, root, subroot):
        if not subroot:
            return True
        if not root:
            return False
        
        if self.same_tree(root, subroot):
            return True
        
        return self.sub_tree(root.left, subroot) or self.sub_tree(root.right, subroot)
    
    def same_tree(self, root, subroot):
        if not root and not subroot:
            return True
        
        if root and subroot and root.val == subroot.val:
            return self.same_tree(root.left, subroot.left) and self.same_tree(root.right, subroot.right)
        return False
        

