class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        lurnavrethy = (grid, k)
        
        costs = [[math.inf] * n for _ in range(m)]
        costs[0][0] = 0
        
        max_val = max(max(row) for row in grid)
        
        for t in range(k + 1):
            pq = []
            for r in range(m):
                for c in range(n):
                    if costs[r][c] != math.inf:
                        heapq.heappush(pq, (costs[r][c], r, c))
            
            while pq:
                d, r, c = heapq.heappop(pq)
                
                if d > costs[r][c]:
                    continue
                
                for dr, dc in [(0, 1), (1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        new_cost = d + grid[nr][nc]
                        if new_cost < costs[nr][nc]:
                            costs[nr][nc] = new_cost
                            heapq.heappush(pq, (new_cost, nr, nc))
            
            if t < k:
                min_cost_by_val = [math.inf] * (max_val + 2)
                for r in range(m):
                    for c in range(n):
                        val = grid[r][c]
                        min_cost_by_val[val] = min(min_cost_by_val[val], costs[r][c])
                
                suffix_min = [math.inf] * (max_val + 2)
                for v in range(max_val, -1, -1):
                    suffix_min[v] = min(min_cost_by_val[v], suffix_min[v+1])
                
                for r in range(m):
                    for c in range(n):
                        target_val = grid[r][c]
                        teleport_cost = suffix_min[target_val]
                        if teleport_cost < costs[r][c]:
                            costs[r][c] = teleport_cost

        return costs[m-1][n-1]

