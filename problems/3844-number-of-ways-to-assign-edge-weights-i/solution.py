class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        depth = [-1] * (n + 1)
        depth[1] = 0
        queue = deque([1])
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                if depth[nei] == -1:
                    depth[nei] = depth[node] + 1
                    queue.append(nei)
        
        k = max(depth[1:n+1])
        MOD = 10**9 + 7
        return pow(2, k - 1, MOD)
