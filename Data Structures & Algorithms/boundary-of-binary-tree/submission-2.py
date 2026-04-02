# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, is_left_boundary, is_right_boundary):
            if not node:
                return
            
            is_leaf = not node.left and not node.right

            # For right boundary, we'll add in reverse order later
            if is_left_boundary and not is_leaf:
                res.append(node.val)
            
            if is_leaf:
                res.append(node.val)

            # Determine flags for children
            left_child_left_boundary = is_left_boundary
            left_child_right_boundary = is_right_boundary and not node.right

            right_child_left_boundary = is_left_boundary and not node.left
            right_child_right_boundary = is_right_boundary

            dfs(node.left, left_child_left_boundary, left_child_right_boundary)
            dfs(node.right, right_child_left_boundary, right_child_right_boundary)

            if is_right_boundary and not is_leaf:
                res.append(node.val)

        if not root:
            return res
        res.append(root.val)
        dfs(root.left, True, False)
        dfs(root.right, False, True)
        return res

