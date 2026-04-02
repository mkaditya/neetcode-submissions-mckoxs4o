class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        def is_leaf(node):
            return not node.left and not node.right

        # 1. root
        if not is_leaf(root):
            res.append(root.val)

        # 2. left boundary (exclude leaves)
        def add_left(node):
            while node:
                if not is_leaf(node):
                    res.append(node.val)
                if node.left:
                    node = node.left
                else:
                    node = node.right

        # 3. leaves
        def add_leaves(node):
            if not node:
                return
            if is_leaf(node):
                res.append(node.val)
                return
            add_leaves(node.left)
            add_leaves(node.right)

        # 4. right boundary (stack for reverse order)
        def add_right(node):
            stack = []
            while node:
                if not is_leaf(node):
                    stack.append(node.val)
                if node.right:
                    node = node.right
                else:
                    node = node.left
            while stack:
                res.append(stack.pop())

        if root.left:
            add_left(root.left)

        add_leaves(root)

        if root.right:
            add_right(root.right)

        return res