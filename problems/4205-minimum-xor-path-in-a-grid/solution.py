class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        dp = [{grid[0][0]}] + [set() for _ in range(len(grid[0]) - 1)]
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if i == j == 0: continue
                dp[j] = {v ^ val for v in (dp[j] if i else set()) | (dp[j-1] if j else set())}
        return min(dp[-1])
