class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        for i in range(len(s)):
            for j in range(i + 1, min(i + k + 1, len(s))):
                if s[i] == s[j]:
                    return self.mergeCharacters(s[:j] + s[j+1:], k)

        return s
