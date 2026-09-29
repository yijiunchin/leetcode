class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n) % 2 == 0 or grid[0][0] == ')' or grid[-1][-1] == '(':
            return False
        
        dp = [0] * n
        dp[0] = 1
        
        for i in range(m):
            for j in range(n):
                mask = dp[j] | (dp[j - 1] if j > 0 else 0)
                dp[j] = mask << 1 if grid[i][j] == '(' else mask >> 1
                
        return bool(dp[-1] & 1)
