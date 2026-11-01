class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7
        nxt = [[0, 0] for _ in range(n + 1)]
        
        for r in range(m - 1, -1, -1):
            cur = [[0, 0] for _ in range(n + 1)]
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    cur[c] = [1, 1]
                elif grid[r][c] == 1:
                    cur[c] = [nxt[c][1], cur[c + 1][0]]
                else:
                    paths = (cur[c + 1][0] + nxt[c][1]) % mod
                    cur[c] = [paths, paths]
            nxt = cur
            
        return nxt[0][0]
