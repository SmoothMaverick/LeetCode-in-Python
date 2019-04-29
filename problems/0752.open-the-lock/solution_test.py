import unittest
from solution import Solution


class TestOpenTheLock(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"nums": [2, 7, 11, 15], "target": 9, "answer": [0, 1]},
            {"nums": [1, 8, 13, 38], "target": 21, "answer": [1, 2]},
            {"nums": [10, 1, 25, 99], "target": 100, "answer": [1, 3]},
            {"nums": [0, 0], "target": 0, "answer": [0, 1]},
        ]

    def test_solution(self):
        soln = Solution()
        for test in self.test_cases:
            result = soln.twoSum(test["nums"], test["target"])
            self.assertEqual(result, test["answer"])


if __name__ == "__main__":
    unittest.main()
