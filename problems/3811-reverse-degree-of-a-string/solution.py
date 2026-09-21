class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((123 - ord(c)) * i for i, c in enumerate(s, 1))
