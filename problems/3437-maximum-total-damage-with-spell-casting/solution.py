class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        count = Counter(power)
        dmg = {power:power * count[power] for power in count}
        spell = [0]*3 + sorted(list(count.keys()))
        n = len(spell)
        dp = [0] * n
        for i in range(3, n):
            if spell[i] - spell[i-1] > 2:
                dp[i] = dp[i-1] + dmg[spell[i]]
            elif spell[i] - spell[i-2] > 2:
                dp[i] = max(
                    dp[i-1],
                    dp[i-2] + dmg[spell[i]],
                )
            else: dp[i] = max(dp[i-1], dp[i-3] + dmg[spell[i]])
        return dp[-1]

