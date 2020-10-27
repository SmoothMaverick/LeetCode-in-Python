import pytest
from solution import Solution
from solution import Recursive


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "0", "1", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "1", "0", "1"],
            ],
            3,
        ),
    ],
)
def test_revese(test_input, expected):
    assert Solution().numIslands(test_input) == expected
    assert Recursive().numIslands(test_input) == expected