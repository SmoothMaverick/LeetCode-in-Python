import pytest
from solution import Recursive, Iterative, TreeNode

test_data = [
    ([], []),
    ([1], [1]),
    ([1, 2], [2, 1]),
    ([1, None, 2], [1, 2]),
    ([3, 1, 2], [1, 3, 2]),
    ([1, None, 2, 3], [1, 3, 2]),
    ([2, 1, 3, None, 4], [1, 4, 2, 3]),
]


def makeTree(input) -> TreeNode:
    root = None
    queue = []

    if len(input) > 0:
        root = TreeNode(input[0])
        queue.append(root)

        for i in range(1, len(input), 2):
            j = i + 1
            node = queue.pop()

            if len(input) > j and input[j]:
                node.right = TreeNode(input[j])
                queue.append(node.right)

            if input[i]:
                node.left = TreeNode(input[i])
                queue.append(node.left)

    return root


@pytest.mark.parametrize("test_input,expected", test_data)
def test_recursive(test_input, expected):
    root = makeTree(test_input)
    assert Recursive().inorderTraversal(root) == expected


@pytest.mark.parametrize("test_input,expected", test_data)
def test_iterative(test_input, expected):
    root = makeTree(test_input)
    assert Iterative().inorderTraversal(root) == expected
