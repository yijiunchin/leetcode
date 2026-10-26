class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        def bfs(r: int, c: int) -> int:
            total = 0
            queue = [(r, c)]
            grid[r][c] = 0
            for curr_r, curr_c in queue:
                total += orig_val[curr_r][curr_c]
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc]:
                        grid[nr][nc] = 0
                        queue.append((nr, nc))
            return total

        orig_val = [row[:] for row in grid]
        return sum(
            bfs(r, c) % k == 0
            for r in range(m)
            for c in range(n)
            if grid[r][c]
        )
