class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 1: return grid[0][0]

        next_scan = [(0, 0)]
        visited = [[False] * m for _ in range(m)]
        max_n = m * m - 1
        min_n = max(grid[0][0], grid[m - 1][m - 1])

        while next_scan:
            mid_n = int((max_n + min_n) / 2)
            x, y = next_scan.pop(0)
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if grid[nx][ny] <= mid_n:
                        next_scan.append((nx, ny))

                    if visited[m - 1][m - 1]: break

            if not next_scan:
                if visited[m - 1][m - 1]:
                    max_n = mid_n
                else:
                    min_n = mid_n + 1

                if max_n == min_n: return max_n

                next_scan.append((0, 0))
                visited = [[False] * m for _ in range(m)]

