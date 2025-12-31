class Solution:
    def latestDayToCross(
        self, row: int, col: int, cells: list[list[int]]
    ) -> int:
        left, right = 0, len(cells)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if self._can_cross(row, col, mid, cells):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

    def _can_cross(self, row, col, day, cells):
        grid = [[0] * col for _ in range(row)]
        for i in range(day):
            r, c = cells[i]
            grid[r - 1][c - 1] = 1

        queue = collections.deque()
        for c in range(col):
            if grid[0][c] == 0:
                queue.append((0, c))
                grid[0][c] = 1

        while queue:
            r, c = queue.popleft()
            if r == row - 1:
                return True
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr, nc))
        return False

