class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        LOG = 18
        up = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        q = [(1, 0)]
        while q:
            nxt = []
            for u, p in q:
                for v in adj[u]:
                    if v != p:
                        depth[v] = depth[u] + 1
                        up[v][0] = u
                        nxt.append((v, u))
            q = nxt
            
        for j in range(1, LOG):
            for i in range(1, n + 1):
                up[i][j] = up[up[i][j-1]][j-1]
                
        def get_lca(u, v):
            if depth[u] < depth[v]: 
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1: 
                    u = up[u][j]
            if u == v: 
                return u
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u, v = up[u][j], up[v][j]
            return up[u][0]
            
        MOD = 10**9 + 7
        p2 = [1] * (n + 1)
        for i in range(1, n + 1):
            p2[i] = (p2[i-1] * 2) % MOD
            
        return [0 if u == v else p2[depth[u] + depth[v] - 2 * depth[get_lca(u, v)] - 1] for u, v in queries]
