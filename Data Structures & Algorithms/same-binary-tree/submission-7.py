# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # return self.is_same_iteration(p, q)
        return self.practice(p, q)

    def practice(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return (p.val == q.val and self.practice(p.left, q.left) and self.practice(p.right, q.right))

    def is_same(self, p, q):
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.is_same(p.left, q.left) and self.is_same(p.right, q.right)
        else:
            return False

    def is_same_iteration(self, p, q):
        if not p and not q:
            return True
        
        stack = [(p, q)]
        while stack:
            t1, t2 = stack.pop()
            if not t1 and not t2:
                continue
            if t1 and t2 and t1.val == t2.val:
                stack.append((t1.left, t2.left))
                stack.append((t1.right, t2.right))
            else:
                return False
        return True