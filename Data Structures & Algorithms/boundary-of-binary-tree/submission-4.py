class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        self.res = []

        # 1. root
        if not self.is_leaf(root):
            self.res.append(root.val)

        # 2. left boundary
        self.add_left(root.left)

        # 3. leaves
        self.add_leaves(root)

        # 4. right boundary
        self.add_right(root.right)

        return self.res

    def is_leaf(self, node):
        return node and not node.left and not node.right

    def add_left(self, node):
        while node:
            if not self.is_leaf(node):
                self.res.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right

    def add_leaves(self, node):
        if not node:
            return
        if self.is_leaf(node):
            self.res.append(node.val)
            return
        self.add_leaves(node.left)
        self.add_leaves(node.right)

    def add_right(self, node):
        stack = []
        while node:
            if not self.is_leaf(node):
                stack.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left

        while stack:
            self.res.append(stack.pop())