class Solution:
    def largestEven(self, s: str) -> str:
        if s[-1] == '2': return s
        while s and s[-1] == '1':
            s = s[:-1]
        return s

