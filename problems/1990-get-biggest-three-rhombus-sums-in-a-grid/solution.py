class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = set()
        
        for i in range(m):
            for j in range(n):
                res.add(grid[i][j])
                L = 1
                while i + 2 * L < m and 0 <= j - L and j + L < n:
                    res.add(sum(
                        grid[i + k][j + k] + 
                        grid[i + L + k][j + L - k] + 
                        grid[i + 2 * L - k][j - k] + 
                        grid[i + L - k][j - L + k]
                        for k in range(L)
                    ))
                    L += 1
                    
        return sorted(res, reverse=True)[:3]
