class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1] * (k + 1) for _ in range(n)]
        dp[0][0] = 0
        
        for i in range(m):
            for j in range(n):
                if not i and not j:
                    continue
                
                v = grid[i][j]
                dc, ds = (1, v) if v else (0, 0)
                nxt = [-1] * (k + 1)
                
                for c in range(dc, min(k, i + j) + 1):
                    t = dp[j][c - dc] if i else -1
                    l = dp[j - 1][c - dc] if j else -1
                    mx = t if t > l else l
                    
                    if mx != -1:
                        nxt[c] = mx + ds
                        
                dp[j] = nxt
                
        return max(dp[-1])
