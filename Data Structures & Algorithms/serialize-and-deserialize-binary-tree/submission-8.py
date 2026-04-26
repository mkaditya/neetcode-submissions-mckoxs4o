# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def __init__(self):
        self.delimiter = ","
        self.null_node = "#"
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return self.null_node
        return str(root.val) + self.delimiter + self.serialize(root.left) + self.delimiter + self.serialize(root.right)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(self.delimiter)
        idx = 0

        def construct():
            nonlocal idx
            if idx >= len(values) or values[idx] == "#":
                idx += 1
                return None
            node = TreeNode(int(values[idx]))
            idx += 1
            node.left = construct()
            node.right = construct()
            return node
        
        return construct()

