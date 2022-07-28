class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        x = str(x)
        if x[0] == '-':
            x = x[1:]
            sign = -1
        x = x[::-1]
        print(x)
        if int(x) >= 2**31 -1:
            return 0
        return sign * int(x)
        