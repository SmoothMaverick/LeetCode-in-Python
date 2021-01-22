from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Recursive:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []

        def traverse(root: TreeNode):
            if root.left:
                traverse(root.left)

            output.append(root.val)

            if root.right:
                traverse(root.right)

            return

        if root:
            traverse(root)

        return output


class Iterative:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        stack = []
        node = root

        while node or stack:
            while node != None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                output.append(node.val)
                node = node.right

        return output
