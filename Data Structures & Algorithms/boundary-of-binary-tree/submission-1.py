# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, is_left, is_right):
            if not node:
                return
            
            is_leaf = not node.left and not node.right
            if is_left and not is_leaf:
                res.append(node.val)

            if is_leaf:
                res.append(node.val)
            
            dfs(node.left, is_left, is_right and not node.right)
            dfs(node.right, is_left and not node.left, is_right)

            if is_right and not is_leaf:
                res.append(node.val)

        if not root:
            return res
        res.append(root.val)
        dfs(root.left, True, False)
        dfs(root.right, False, True)
        return res
