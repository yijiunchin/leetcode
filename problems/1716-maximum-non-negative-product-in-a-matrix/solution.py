class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        dp = [[(0, 0)] * len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = (grid[0][0], grid[0][0])
        
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if not i and not j: 
                    continue
                c = [dp[r][c][k] * val for r, c in ((i-1, j), (i, j-1)) if r >= 0 and c >= 0 for k in (0, 1)]
                dp[i][j] = (min(c), max(c))
                
        ans = dp[-1][-1][1]
        return ans % (10**9 + 7) if ans >= 0 else -1
