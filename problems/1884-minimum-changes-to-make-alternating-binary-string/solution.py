class Solution:
    def minOperations(self, s: str) -> int:
        cnt = sum(c != str(i % 2) for i, c in enumerate(s))
        return min(cnt, len(s) - cnt)
