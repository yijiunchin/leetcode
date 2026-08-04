class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * 3
        for i in range(n - 1, -1, -1):
            dp[i % 3] = max(
                sum(stoneValue[i : i + k]) - dp[(i + k) % 3]
                for k in range(1, min(4, n - i + 1))
            )
        return 'Alice' if dp[0] > 0 else 'Bob' if dp[0] < 0 else 'Tie'
