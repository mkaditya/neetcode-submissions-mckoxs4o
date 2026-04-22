# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def __init__(self):
        self.empty_node = "#"
        self.delimiter = ","
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        
        def dfs(node):
            if not node:
                result.append(self.empty_node)
                return
            
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.delimiter.join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(self.delimiter)
        total_len = len(values)
        curr_idx = 0

        def dfs():
            nonlocal curr_idx
            if curr_idx >= total_len or values[curr_idx] == self.empty_node:
                curr_idx += 1
                return None
            
            node = TreeNode(int(values[curr_idx]))
            curr_idx += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

