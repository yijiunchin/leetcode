class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        dp = [True] + [False] * (len(s) - 1)
        pre_sum = 0
        for i in range(1, len(s)):
            if i >= minJump:
                pre_sum += dp[i - minJump]
            if i > maxJump:
                pre_sum -= dp[i - maxJump - 1]
            dp[i] = pre_sum > 0 and s[i] == '0'
        return dp[-1]
