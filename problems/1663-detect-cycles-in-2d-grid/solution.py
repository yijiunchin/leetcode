class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        p = list(range(m * n))
        
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
            
        for i in range(m):
            for j in range(n):
                curr = i * n + j
                if i > 0 and grid[i][j] == grid[i-1][j]:
                    r1, r2 = find(curr), find(curr - n)
                    if r1 == r2:
                        return True
                    p[r1] = r2
                if j > 0 and grid[i][j] == grid[i][j-1]:
                    r1, r2 = find(curr), find(curr - 1)
                    if r1 == r2:
                        return True
                    p[r1] = r2
                    
        return False
