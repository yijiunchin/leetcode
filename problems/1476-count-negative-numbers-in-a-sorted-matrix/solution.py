class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        find = len(grid[-1])
        neg = 0
        for i in range(len(grid) - 1, -1, -1):
            sub_neg = 0
            for j in range(len(grid[i]) - 1, len(grid[i]) - find - 1, -1):
                if grid[i][j] >= 0: break
                sub_neg += 1
            neg += sub_neg
        return neg

