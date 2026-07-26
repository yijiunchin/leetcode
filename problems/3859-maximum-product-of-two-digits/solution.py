class Solution:
    def maxProduct(self, n: int) -> int:
        d = sorted(str(n))
        return int(d[-1]) * int(d[-2])
