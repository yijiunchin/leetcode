class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        pq = []
        total_water = 0

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(pq, (heightMap[i][j], i, j))
                    visited[i][j] = True

        while pq:
            height, r, c = heapq.heappop(pq)
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    if height > heightMap[nr][nc]:
                        total_water += height - heightMap[nr][nc]

                    heapq.heappush(pq, (max(height, heightMap[nr][nc]), nr, nc))
                    visited[nr][nc] = True

        return total_water

