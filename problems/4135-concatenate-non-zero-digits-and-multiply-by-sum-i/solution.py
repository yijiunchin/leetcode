class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n).replace('0', '')
        return int(s) * sum(map(int, s)) if s else 0
