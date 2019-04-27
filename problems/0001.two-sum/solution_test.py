import unittest
from solution import Solution


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.test_cases = [{"nums": [2, 7, 11, 15], "target": 9}]

    def test_two_sum(self):
        soln = Solution()
        for test in self.test_cases:
            result = soln.twoSum(test["nums"], test["target"])
            self.assertEqual(result, 9)


if __name__ == "__main__":
    unittest.main()
