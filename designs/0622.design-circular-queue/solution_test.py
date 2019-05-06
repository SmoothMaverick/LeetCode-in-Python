import pytest

from solution import MyCircularQueue

test_cases = [
    [
        3,
        ["enQueue", 1, True],
        ["enQueue", 2, True],
        ["enQueue", 3, True],
        ["enQueue", 4, False],
        ["Rear", None, 3],
        ["isFull", None, True],
        ["deQueue", None, True],
        ["enQueue", 4, True],
        ["Rear", None, 4],
    ]
]


@pytest.mark.parametrize("test_case", test_cases)
def test_circular_queue(test_case):
    size = test_case[0]
    queue = MyCircularQueue(size)

    for test in test_case[1:]:
        func = test[0]
        param = test[1]
        expected = test[2]
        if param == None:
            assert getattr(queue, func)() == expected
        else:
            assert getattr(queue, func)(param) == expected

