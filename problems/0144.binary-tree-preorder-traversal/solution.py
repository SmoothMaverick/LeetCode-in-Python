from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Recursive:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        output = []

        def traverse(root: TreeNode):
            output.append(root.val)

            if root.left:
                traverse(root.left)

            if root.right:
                traverse(root.right)

            return

        if root:
            traverse(root)

        return output


class Iterative:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        queue = []

        if root:
            queue.append(root)

        while queue:
            root = queue.pop()
            output.append(root.val)

            if root.right:
                queue.append(root.right)

            if root.left:
                queue.append(root.left)

        return output
