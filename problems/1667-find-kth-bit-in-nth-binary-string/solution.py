class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        inv = 0
        while n > 1:
            mid = 1 << (n - 1)
            if k == mid:
                return str(1 ^ inv)
            if k > mid:
                k = (1 << n) - k
                inv ^= 1
            n -= 1
        return str(inv)
