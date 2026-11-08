class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        row_cnt = [sum(row) for row in grid]
        col_cnt = [sum(col) for col in zip(*grid)]
        return sum(
            1
            for i, row in enumerate(grid)
            for j, val in enumerate(row)
            if val and (row_cnt[i] > 1 or col_cnt[j] > 1)
        )
