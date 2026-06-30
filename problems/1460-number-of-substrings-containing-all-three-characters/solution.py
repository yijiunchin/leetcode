class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = [-1, -1, -1]
        ans = 0
        for i, char in enumerate(s):
            last[ord(char) - 97] = i
            ans += min(last) + 1
        return ans
