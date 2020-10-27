from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        size = len(s)

        for i in range(int(size / 2)):
            j = size - 1 - i
            s[i], s[j] = s[j], s[i]

        return None


class Recursive:
    def reverseString(self, s: List[str]) -> None:
        self.helper(0, s)

    def helper(self, i: int, s: List[str]):
        if i >= len(s) / 2:
            return

        self.helper(i + 1, s)

        j = len(s) - 1 - i
        s[i], s[j] = s[j], s[i]
