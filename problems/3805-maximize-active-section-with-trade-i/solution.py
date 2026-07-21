class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        zeros = [len(x) for x in s.split('1') if x]
        if len(zeros) < 2:
            return s.count('1')
        return s.count('1') + max(a + b for a, b in zip(zeros, zeros[1:]))
