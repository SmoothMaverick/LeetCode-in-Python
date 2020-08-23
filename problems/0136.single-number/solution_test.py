import pytest

from solution import Solution


@pytest.mark.parametrize("test_input,expected", [[[2, 2, 1], 1], [[4, 1, 2, 1, 2], 4]])
def test_revese(test_input, expected):
    assert Solution().singleNumber(test_input) == expected
