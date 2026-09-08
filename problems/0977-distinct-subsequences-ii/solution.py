class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [0] * 26
        mod = 10**9 + 7
        for char in s:
            dp[ord(char) - 97] = (sum(dp) + 1) % mod
        return sum(dp) % mod
