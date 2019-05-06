class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            y = str(x)
            x = int(y[::-1])
        elif x < 0:
            y = str(-1 * x)
            x = int(y[::-1])
            x = x * -1
        else:
            return 0

        if (x > 2 ** 31 - 1) or (x < -2 ** 31):
            return 0

        return x
