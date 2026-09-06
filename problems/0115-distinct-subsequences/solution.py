class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [1] + [0] * len(t)
        for char in s:
            for j in range(len(t) - 1, -1, -1):
                if char == t[j]:
                    dp[j + 1] += dp[j]
        return dp[-1]
