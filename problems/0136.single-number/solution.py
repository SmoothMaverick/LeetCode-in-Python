from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        1. create a "seen" set
        2. loop through "nums" list
        3. numbers that have not been observed, are added to "seen"
        4. numbers that have already been observed, are removed from "seen"
        5. loop through "seen" dictionary, which should only have one value
        6. return first value
        """

        seen = set()

        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)

        for num in seen:
            return num
