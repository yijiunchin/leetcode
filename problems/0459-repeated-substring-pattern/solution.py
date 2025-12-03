class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s) // 2):
            c = s[: i + 1]
            clen = len(s[: i + 1])
            if c * (len(s) // len(s[: i + 1])) == s:
                return True
        return False

