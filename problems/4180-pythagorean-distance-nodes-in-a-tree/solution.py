class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        mapping = [[] for _ in range(n)]
        for u, v in edges:
            mapping[u].append(v)
            mapping[v].append(u)

        def get_d(start):
            d = [-1] * n
            d[start] = 0
            q = deque([start])
            while q:
                current = q.popleft()
                for m in mapping[current]:
                    if d[m] == -1:
                        d[m] = d[current] + 1
                        q.append(m)

            return d

        dx = get_d(x)
        dy = get_d(y)
        dz = get_d(z)
        count = 0
        for u in range(n):
            d = sorted([dx[u], dy[u], dz[u]])
            if d[0] ** 2 + d[1] ** 2 == d[2] ** 2:
                count += 1

        return count

