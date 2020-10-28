import pytest

from solution import ListNode, Solution


def run_test(test_input, expected, solution):
    head = None
    curr = None

    for val in test_input:
        if curr == None:
            curr = ListNode(val)
            head = curr
        else:
            curr.next = ListNode(val)
            curr = curr.next

    new_head = solution().swapPairs(head)

    for i, val in enumerate(expected):
        msg = "i:", i
        assert new_head.val == val, msg
        new_head = new_head.next


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [2, 1, 3]),
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([0, 10, 100, 1000], [10, 0, 1000, 100]),
    ],
)
def test_solution(test_input, expected):
    run_test(test_input, expected, Solution)
