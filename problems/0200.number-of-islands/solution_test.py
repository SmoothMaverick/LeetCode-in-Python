import unittest
from solution import Solution
from solution import Recursive


class TestNumIslands(unittest.TestCase):
    def setUp(self):
        self.test_case = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]

    def test_solution(self):
        soln = Solution()
        result = soln.numIslands(self.test_case)
        self.assertEqual(result, 1)

    def test_recursive(self):
        soln = Recursive()
        result = soln.numIslands(self.test_case)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
