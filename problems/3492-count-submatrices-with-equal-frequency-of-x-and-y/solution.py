class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        ans = 0
        col_x = [0] * len(grid[0])
        col_y = [0] * len(grid[0])
        
        for row in grid:
            x = y = 0
            for j, val in enumerate(row):
                col_x[j] += val == 'X'
                col_y[j] += val == 'Y'
                x += col_x[j]
                y += col_y[j]
                ans += x == y and x > 0
                
        return ans
