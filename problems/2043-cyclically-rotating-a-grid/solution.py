class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        for i in range(min(m, n) // 2):
            t, b, l, r = i, m - i - 1, i, n - i - 1
            
            pos = (
                [(t, c) for c in range(l, r + 1)]
                + [(x, r) for x in range(t + 1, b)]
                + [(b, c) for c in range(r, l - 1, -1)]
                + [(x, l) for x in range(b - 1, t, -1)]
            )
            
            vals = [grid[x][y] for x, y in pos]
            step = k % len(vals)
            vals = vals[step:] + vals[:step]
            
            for (x, y), v in zip(pos, vals):
                grid[x][y] = v
                
        return grid
