class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        div = [[] for _ in range(n + 1)]
        for i in range(1, n):
            for j in range(i * 2, n + 1, i):
                div[j].append(i)
        cost = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1):
            for j in range(i + 2, n + 1):
                c_min = n
                for d in div[j - i]:
                    c = 0
                    for r in range(d):
                        lt, rt = i + r, j - d + r
                        while lt < rt:
                            if s[lt] != s[rt]:
                                c += 1
                            lt += d
                            rt -= d
                    if c < c_min:
                        c_min = c
                cost[i][j] = c_min
        dp = [n] * (n + 1)
        dp[0] = 0
        for m in range(1, k + 1):
            nxt = [n] * (n + 1)
            for i in range(m * 2, n + 1):
                nxt[i] = min(
                    dp[p] + cost[p][i] for p in range((m - 1) * 2, i - 1)
                )
            dp = nxt
        return dp[n]
