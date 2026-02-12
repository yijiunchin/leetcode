class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        groups = collections.defaultdict(list)
        for r in range(m):
            for c in range(n):
                groups[grid[r][c]].append((r, c))

        sorted_vals = sorted(groups.keys(), reverse=True)
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = 0
        ans = float('inf')
        for _ in range(k + 1):
            for r in range(m):
                for c in range(n):
                    curr = dp[r][c]
                    if r > 0 and dp[r - 1][c] + grid[r][c] < curr:
                        curr = dp[r - 1][c] + grid[r][c]
                    if c > 0 and dp[r][c - 1] + grid[r][c] < curr:
                        curr = dp[r][c - 1] + grid[r][c]
                    dp[r][c] = curr

            ans = min(ans, dp[m - 1][n - 1])
            if _ < k:
                next_dp = [[float('inf')] * n for _ in range(m)]
                min_val = float('inf')
                for val in sorted_vals:
                    group_min = float('inf')
                    for r, c in groups[val]:
                        if dp[r][c] < group_min:
                            group_min = dp[r][c]

                    if group_min < min_val:
                        min_val = group_min

                    for r, c in groups[val]:
                        next_dp[r][c] = min_val

                dp = next_dp

        return ans

