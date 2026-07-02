class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        dq = deque([(0, 0)])

        while dq:
            r, c = dq.popleft()
            if r == m - 1 and c == n - 1:
                return dist[r][c] < health

            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    cost = dist[r][c] + grid[nr][nc]
                    if cost < dist[nr][nc] and cost < health:
                        dist[nr][nc] = cost
                        if grid[nr][nc] == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))

        return False
