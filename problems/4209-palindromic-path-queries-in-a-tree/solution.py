class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        depth = [0] * n
        parent = [[-1] * 20 for _ in range(n)]
        tin = [0] * n
        tout = [0] * n
        timer = 0
        node = [1 << (ord(c) - ord('a')) for c in s]

        def dfs(u, p, d):
            nonlocal timer
            timer += 1
            tin[u] = timer
            depth[u] = d
            parent[u][0] = p
            for i in range(1, 20):
                if parent[u][i - 1] != -1:
                    parent[u][i] = parent[parent[u][i - 1]][i - 1]
                else:
                    parent[u][i] = -1

            for v in adj[u]:
                if v != p:
                    dfs(v, u, d + 1)

            tout[u] = timer

        dfs(0, -1, 0)

        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for i in range(19, -1, -1):
                if depth[u] - (1 << i) >= depth[v]:
                    u = parent[u][i]

            if u == v:
                return u

            for i in range(19, -1, -1):
                if parent[u][i] != parent[v][i]:
                    u = parent[u][i]
                    v = parent[v][i]

            return parent[u][0]

        bit = [0] * (n + 2)

        def update_bit(i, val):
            while i <= n + 1:
                bit[i] ^= val
                i += i & (-i)

        def query_bit(i):
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & (-i)

            return res

        def range_update(l, r, val):
            update_bit(l, val)
            update_bit(r + 1, val)

        for i in range(n):
            range_update(tin[i], tout[i], node[i])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == 'update':
                u = int(parts[1])
                val = 1 << (ord(parts[2]) - ord('a'))
                diff = node[u] ^ val
                if diff:
                    range_update(tin[u], tout[u], diff)
                    node[u] = val
            else:
                u, v = int(parts[1]), int(parts[2])
                lca = get_lca(u, v)
                path = query_bit(tin[u]) ^ query_bit(tin[v]) ^ node[lca]
                ans.append(path == 0 or (path & (path - 1)) == 0)

        return ans
