# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node):
            if not node:
                return
            
            inorder(node.left) # stack.append()
            node_vals.append(node.val)
            inorder(node.right) # stack.append()

        def inorder_iterative(node):
            curr_node = node
            stack = []
            while curr_node or stack:
                # Simulate inorder(node.left) - go all the way left
                while curr_node:
                    stack.append(curr_node)
                    curr_node = curr_node.left
                
                # Simulate processing the current node
                curr_node = stack.pop()
                node_vals.append(curr_node.val)

                # Simulate inorder(node.right) - go right
                curr_node = curr_node.right
                    
        node_vals = []
        inorder_iterative(root)
        return node_vals
            
