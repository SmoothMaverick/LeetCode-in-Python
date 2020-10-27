import pytest

from solution import Solution, Recursive


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["a", "l", "e", "x"], ["x", "e", "l", "a"]),
        (["a", "b", "c"], ["c", "b", "a"]),
    ],
)
def test_revese(test_input, expected):
    Solution().reverseString(test_input)
    assert test_input == expected
    Solution().reverseString(test_input)

    Recursive().reverseString(test_input)
    assert test_input == expected
    Recursive().reverseString(test_input)
