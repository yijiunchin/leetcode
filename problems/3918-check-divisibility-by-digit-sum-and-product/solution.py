class Solution:
    def checkDivisibility(self, n: int) -> bool:
        a = 0
        b = 1
        for m in str(n):
            a += int(m)
            b *= int(m)

        if n % (a + b) == 0:
            return True

        return False
