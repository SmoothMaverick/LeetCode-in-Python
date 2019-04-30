import unittest
from solution import Solution


class TestOpenTheLock(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"deadends": ["7777"], "target": "0000", "expected": 0},
            {"deadends": ["8888"], "target": "0009", "expected": 1},
            {"deadends": ["0000"], "target": "8888", "expected": -1},
            {
                "deadends": ["0201", "0101", "0102", "1212", "2002"],
                "target": "0202",
                "expected": 6,
            },
            {
                "deadends": [
                    "8887",
                    "8889",
                    "8878",
                    "8898",
                    "8788",
                    "8988",
                    "7888",
                    "9888",
                ],
                "target": "8888",
                "expected": -1,
            },
        ]

    def runTest(self):
        for i, test in enumerate(self.test_cases):
            with self.subTest(i=i, target=test["target"]):
                result = Solution().openLock(test["deadends"], test["target"])
                self.assertEqual(result, test["expected"])


if __name__ == "__main__":
    unittest.main()
