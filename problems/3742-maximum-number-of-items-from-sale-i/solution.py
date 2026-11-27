class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        cnt = Counter(f for f, _ in items)
        max_f = max(cnt)
        val = {f: sum(cnt[m] for m in range(f, max_f + 1, f)) for f in cnt}

        dp = [0] * (budget + 1)
        for f, p in items:
            v = val[f]
            for w in range(budget, p - 1, -1):
                if dp[w - p] + v > dp[w]:
                    dp[w] = dp[w - p] + v

        min_p = min(p for _, p in items)
        return max(dp[w] + (budget - w) // min_p for w in range(budget + 1))
