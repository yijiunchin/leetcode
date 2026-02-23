class Solution:
    def binaryGap(self, n: int) -> int:
        idx = [i for i, x in enumerate(bin(n)) if x == '1']
        return max((b - a for a, b in zip(idx, idx[1:])), default=0)
