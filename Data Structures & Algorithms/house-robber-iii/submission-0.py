# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = defaultdict(int)

        def dfs(node):
            if not node:
                return 0
            if node in cache:
                return cache[node]
            
            curr_included_steal = node.val # min value by robbing current node
            if node.right:
                curr_included_steal += dfs(node.right.right) + dfs(node.right.left)
            if node.left:
                curr_included_steal += dfs(node.left.left) + dfs(node.left.right)
            
            curr_excluded_steal = dfs(node.left) + dfs(node.right)

            cache[node] = max(curr_included_steal, curr_excluded_steal) # total current steal vs not choosing ccurrent
            return cache[node]
        return dfs(root)