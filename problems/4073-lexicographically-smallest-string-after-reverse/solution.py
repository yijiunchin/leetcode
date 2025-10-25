class Solution:
    def lexSmallest(self, s: str) -> str:
        ans = s
        for i in range(len(s)):
            left = s[0:i][::-1]
            right = s[i:]
            ans = min(ans, left + right)
            left = s[0:i]
            right = s[i:][::-1]
            ans = min(ans, left + right)
        return ans

