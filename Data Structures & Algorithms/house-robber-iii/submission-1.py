class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}

        def dfs(node):
            if not node:
                return 0
            if node in cache:
                return cache[node]

            # Choice 1: rob this node
            # must skip children, so recurse to grandchildren
            rob_current = node.val
            if node.left:
                rob_current += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                rob_current += dfs(node.right.left) + dfs(node.right.right)

            # Choice 2: skip this node
            # children are now free to be robbed
            skip_current = dfs(node.left) + dfs(node.right)

            cache[node] = max(rob_current, skip_current)
            return cache[node]

        return dfs(root)