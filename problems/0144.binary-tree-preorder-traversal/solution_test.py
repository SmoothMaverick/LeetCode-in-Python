import pytest
from solution import Solution


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([1, null, 2, 3], [1, 2, 3]),
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, null, 2], [1, 2]),
    ],
)
def test_revese(test_input, expected):
    assert Solution().preorderTraversal(test_input) == expected
