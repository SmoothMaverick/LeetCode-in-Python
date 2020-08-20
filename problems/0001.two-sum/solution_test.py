import pytest
from solution import Solution
from solution import BruteForce


@pytest.mark.parametrize(
    "test_input,expected",
    [
        {"nums": [2, 7, 11, 15], "target": 9, "answer": [0, 1]},
        {"nums": [1, 8, 13, 38], "target": 21, "answer": [1, 2]},
        {"nums": [10, 1, 25, 99], "target": 100, "answer": [1, 3]},
        {"nums": [0, 0], "target": 0, "answer": [0, 1]},
    ],
)
def test_revese(test_input, expected):
    assert Solution().twoSum(test_input["nums"], test_input["target"]) == expected
    assert BruteForce().twoSum(test_input["nums"], test_input["target"]) == expected
