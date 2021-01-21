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
        stack = []

        if root:
            stack.append(root)

        while stack:
            root = stack.pop()
            output.append(root.val)

            if root.right:
                stack.append(root.right)

            if root.left:
                stack.append(root.left)

        return output
