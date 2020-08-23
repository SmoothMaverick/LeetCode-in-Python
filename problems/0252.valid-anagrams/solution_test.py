import pytest

from solution import Solution, BruteForce


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ({"s": "anagram", "t": "nagaram"}, True),
        ({"s": "rat", "t": "car"}, False),
        ({"s": "look", "t": "kool"}, True),
        ({"s": "look", "t": "lok"}, False),
    ],
)
def test_revese(test_input, expected):
    assert Solution().isAnagram(test_input["s"], test_input["t"]) == expected
    assert BruteForce().isAnagram(test_input["s"], test_input["t"]) == expected
