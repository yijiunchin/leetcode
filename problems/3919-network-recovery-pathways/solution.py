class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        indeg = [0] * n
        
        for u, v, c in edges:
            if online[u] and online[v]:
                adj[u].append((v, c))
                indeg[v] += 1
                
        topo = []
        q = deque(i for i in range(n) if indeg[i] == 0)
        
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
                    
        costs = sorted({c for u, v, c in edges if online[u] and online[v]})

        def check(m_val: int) -> bool:
            dp = [float('inf')] * n
            dp[0] = 0
            for u in topo:
                if dp[u] == float('inf'):
                    continue
                for v, c in adj[u]:
                    if c >= m_val and dp[u] + c < dp[v]:
                        dp[v] = dp[u] + c
            return dp[n - 1] <= k

        if not check(0):
            return -1

        l, r = 0, len(costs) - 1
        ans = -1
        
        while l <= r:
            m = (l + r) // 2
            if check(costs[m]):
                ans = costs[m]
                l = m + 1
            else:
                r = m - 1
                
        return ans
