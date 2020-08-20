class Solution:
    def reverse(self, x: int) -> int:
        """
            https://leetcode.com/problems/reverse-integer/discuss/798411/Python-3-O(n)-Time-O(1)-Space-with-explanation

            1.  set sign as 1 and if x is less than 0, change sign as -1
            2.  turn it into string and if x < 0 then trim it off index 0: x = x[1:]
            3.  turn x into a list so you can do in place replacement for constant memory space
            4.  Use while loop and two pointer to switch the digits
            5.  turn the list into string by using ''.join(x)
            6.  convert x back to integer and multiply the sign
            7.  If x is not within [-2**31, 2**31-1], return 0
            8.  Otherwise return x

            Time complexity: O(n)
            Space complexity: O(1)
        """

        sign = 1

        if x < 0:
            sign = -1
            x = str(x)[1:]
        else:
            x = str(x)

        x = list(x)

        left = 0
        right = len(x) - 1

        while left < right:
            x[left], x[right] = x[right], x[left]
            left += 1
            right -= 1

        x = "".join(x)
        x = sign * int(x)

        if x < -(2 ** 31) or x > 2 ** 31 - 1:
            return 0

        return x


class BruteForce:
    def reverse(self, x: int) -> int:
        value = ""
        sign = ""

        x = str(x)

        if x[0] == "-":
            sign = "-"
            x = x[1:]

        for num in x:
            value = num + value

        value = int(sign + value)

        if value > 2 ** 31 - 1 or value < -(2 ** 31):
            return 0

        return value
