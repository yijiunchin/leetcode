class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        dp = [0] * (len(s) + 1)
        for i in range(k, len(s) + 1):
            dp[i] = dp[i - 1]
            for j in (i - k, i - k - 1):
                if j >= 0 and s[j:i] == s[j:i][::-1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[-1]
