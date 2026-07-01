class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0
        dist = self._compute_dist(grid, n)
        return self._find_safest(dist, n)

    def _compute_dist(self, grid: list[list[int]], n: int) -> list[list[int]]:
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
                    dist[r][c] = 0
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
        return dist

    def _find_safest(self, dist: list[list[int]], n: int) -> int:
        pq = [(-dist[0][0], 0, 0)]
        dist[0][0] = -1
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        while pq:
            safe, r, c = heapq.heappop(pq)
            if r == n - 1 and c == n - 1:
                return -safe
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] != -1:
                    next_safe = min(-safe, dist[nr][nc])
                    heapq.heappush(pq, (-next_safe, nr, nc))
                    dist[nr][nc] = -1
        return 0
