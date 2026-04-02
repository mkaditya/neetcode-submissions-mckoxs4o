# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)

        def dfs(node):
            if not node:
                return -1 # could be zero but we are treating leaves as o
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            node_height = 1 + max(left_height, right_height)
            res[node_height].append(node.val)
            return node_height
        
        dfs(root)
        return list(res.values())

            