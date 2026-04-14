# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#"
        result = []

        q = deque()
        q.append(root)

        while q:
            curr = q.popleft()
            if curr:
                result.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
            else:
                result.append("#")
            
        return ",".join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "#":
            return None
        vals = data.split(",")

        root = TreeNode(int(vals[0]))
        q = deque()
        q.append(root)
        idx = 1
        while q:
            node = q.popleft()
            if vals[idx] != "#":
                node.left = TreeNode(int(vals[idx]))
                q.append(node.left)
            idx += 1
            
            if vals[idx] != "#":
                node.right = TreeNode(int(vals[idx]))
                q.append(node.right)
            idx += 1
        return root