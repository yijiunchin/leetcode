class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w, False))
            adj[v].append((u, 2 * w, True))

        pq = [(0, 0, 0)]
        dist = {}
        while pq:
            d, u, mask_val = heapq.heappop(pq)
            if d > dist.get((u, mask_val), float('inf')):
                continue
            if u == n - 1:
                return d

            for v, w, is_rev in adj[u]:
                used_u = (mask_val >> 0) & 1 
                if is_rev:
                    if not used_u:
                        new_d = d + w
                        if new_d < dist.get((v, 0), float('inf')):
                            dist[(v, 0)] = new_d
                            heapq.heappush(pq, (new_d, v, 0))
                else:
                    new_d = d + w
                    if new_d < dist.get((v, 0), float('inf')):
                        dist[(v, 0)] = new_d
                        heapq.heappush(pq, (new_d, v, 0))

        return -1

