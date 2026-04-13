# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # return self.level_order(root)
        return self.practice(root)

    def practice(self, node):
        res = []
        q = deque()
        if node:
            q.append(node)

        while q:
            size = len(q)
            curr_level = []
            for _ in range(size):
                node = q.popleft()
                curr_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(curr_level)
        return res

    def level_order(self, root):
        result = []
        q = deque()
        if root:
            q.append(root)

        while q:
            size = len(q)
            level_list = []
            
            for _ in range(size):
                node = q.popleft()
                level_list.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(level_list)
        
        return result
