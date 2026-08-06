class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            x = 1
            for c in str(n):
                x *= int(c)

            if x % t == 0:
                return n

            n += 1

