# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root_node_val = preorder[0]
        root_idx = inorder.index(root_node_val)
        node = TreeNode(root_node_val)
        node.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx]) # mimic same no of elements in preorder
        node.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:]) # mimic same no of elements in preorder
        return node
        