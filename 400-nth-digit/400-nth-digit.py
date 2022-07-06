class Solution:
    def findNthDigit(self, n: int) -> int:
        base = digit = 1
        while n > base*digit*9:
            n -= base*digit*9
            digit += 1
            base *= 10
        div, rem = divmod(n-1,digit)
        return int(str(base + div)[rem])
            