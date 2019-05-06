import pytest

from solution import Solution


@pytest.mark.parametrize(
    "test_input,expected",
    [(123, 321), (-123, -321), (120, 21), (1463847412, 2147483641)],
)
def test_revese(test_input, expected):
    assert Solution().reverse(test_input) == expected
