class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> bool:
            if not (0 <= r < m and 0 <= c < n):
                return False
            if grid[r][c] == 1:
                return True
            grid[r][c] = 1
            res = [dfs(r + dr, c + dc) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))]
            return all(res)

        return sum(
            dfs(i, j)
            for i in range(1, m - 1)
            for j in range(1, n - 1)
            if grid[i][j] == 0
        )
