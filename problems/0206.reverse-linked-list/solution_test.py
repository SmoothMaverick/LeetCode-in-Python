import pytest

from solution import Iterative
from solution import Recursive
from solution import ListNode

test_cases = [
    [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]],
    [[0, 10, 100, 1000], [1000, 100, 10, 0]],
    [[1], [1]],
    [[1, 2], [2, 1]],
]


def run_test(test_input, expected, solution):
    head = None
    curr = None

    for n in test_input:
        if curr == None:
            curr = ListNode(n)
            head = curr
        else:
            curr.next = ListNode(n)
            curr = curr.next

    rev_head = solution().reverseList(head)

    for i, n in enumerate(expected):
        msg = "i:", i
        assert rev_head.val == n, msg
        rev_head = rev_head.next


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_iterative(test_input, expected):
    run_test(test_input, expected, Iterative)


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_recursive(test_input, expected):
    run_test(test_input, expected, Recursive)
