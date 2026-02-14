class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        def dfs(u, p, d):
            nonlocal timer
            timer += 1
            tin[u] = timer
            depth[u] = d
            up[u][0] = p
            for i in range(1, 17):
                if up[u][i - 1] != -1:
                    up[u][i] = up[up[u][i - 1]][i - 1]
            for v in adj[u]:
                if v != p:
                    dfs(v, u, d + 1)
            tout[u] = timer

        def update_bit(idx, val):
            while idx <= n + 1:
                bit[idx] ^= val
                idx += idx & (-idx)

        def query_bit(idx):
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for i in range(16, -1, -1):
                if depth[u] - (1 << i) >= depth[v]:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(16, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        up = [[-1] * 17 for _ in range(n)]
        timer = 0
        dfs(0, -1, 0)
        bit = [0] * (n + 2)
        s_list = list(s)
        vals = [1 << (ord(c) - 97) for c in s_list]
        for i in range(n):
            update_bit(tin[i], vals[i])
            update_bit(tout[i] + 1, vals[i])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == 'update':
                u, c = int(parts[1]), parts[2]
                old_val = vals[u]
                new_val = 1 << (ord(c) - 97)
                xor_diff = old_val ^ new_val
                vals[u] = new_val
                s_list[u] = c
                update_bit(tin[u], xor_diff)
                update_bit(tout[u] + 1, xor_diff)
            else:
                u, v = int(parts[1]), int(parts[2])
                lca = get_lca(u, v)
                path_xor = query_bit(tin[u]) ^ query_bit(tin[v]) ^ vals[lca]
                ans.append(path_xor == 0 or (path_xor & (path_xor - 1)) == 0)

        return ans
