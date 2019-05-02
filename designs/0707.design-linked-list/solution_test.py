import pytest

from solution import MyLinkedList

test_cases = [
    [
        ["addAtHead", [1], None],
        ["get", [0], 1],
        ["addAtTail", [3], None],
        ["get", [1], 3],
        ["addAtIndex", [1, 2], None],
        ["get", [1], 2],
        ["deleteAtIndex", [1], None],
        ["get", [1], 3],
    ],
    [
        ["get", [0], -1],
        ["addAtIndex", [1, 2], None],
        ["get", [1], -1],
        ["addAtIndex", [0, 1], None],
        ["get", [0], 1],
    ],
    [["addAtHead", [1], None], ["deleteAtIndex", [0], None]],
    [
        ["addAtHead", [1], None],
        ["addAtTail", [3], None],
        ["addAtIndex", [1, 2], None],
        ["get", [1], 2],
        ["deleteAtIndex", [0], None],
        ["get", [0], 2],
    ],
    [
        ["addAtIndex", [0, 10], None],
        ["addAtIndex", [0, 20], None],
        ["addAtIndex", [1, 30], None],
        ["get", [0], 20],
    ],
    [["addAtIndex", [-1, 0], None], ["get", [0], 0], ["deleteAtIndex", [-1], None]],
    [
        ["addAtHead", [1], None],
        ["addAtTail", [3], None],
        ["addAtIndex", [4, 2], None],
        ["get", [1], 3],
        ["deleteAtIndex", [-1], None],
        ["get", [1], 3],
    ],
    [
        ["addAtHead", [8], None],
        ["get", [1], -1],
        ["addAtTail", [81], None],
        ["deleteAtIndex", [2], None],
        ["addAtHead", [26], None],
        ["deleteAtIndex", [2], None],
        ["get", [0], 26],
        ["get", [1], 8],
        ["addAtTail", [24], None],
        ["get", [0], 26],
        ["get", [1], 8],
        ["get", [2], 24],
        ["addAtHead", [15], None],
        ["addAtTail", [0], None],
        ["addAtTail", [13], None],
        ["addAtTail", [1], None],
        ["addAtIndex", [6, 33], None],
        ["get", [0], 15],
        ["get", [1], 26],
        ["get", [2], 8],
        ["get", [3], 24],
        ["get", [4], 0],
        ["get", [5], 13],
        ["get", [6], 33],
        ["get", [7], 1],
    ],
]


@pytest.mark.parametrize("test_case", test_cases)
def test_linked_list(test_case):
    obj = MyLinkedList()

    for test in test_case:
        func = test[0]
        param = test[1]
        expected = test[2]

        assert getattr(obj, func)(*param) == expected
