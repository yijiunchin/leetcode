class Solution:
    def _parse(self, grid: List[str]) -> Tuple[Dict[Tuple[int, int], int], Tuple[int, int]]:
        ls = {}
        start = (0, 0)
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 'L':
                    ls[(r, c)] = len(ls)
                elif val == 'S':
                    start = (r, c)
        return ls, start

    def _get_neighbors(self, r: int, c: int, R: int, C: int):
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < R and 0 <= nc < C:
                yield nr, nc

    def minMoves(self, classroom: List[str], energy: int) -> int:
        ls, (sr, sc) = self._parse(classroom)
        req = (1 << len(ls)) - 1
        if not req:
            return 0

        R, C = len(classroom), len(classroom[0])
        q = deque([(sr, sc, 0, energy, 0)])
        vis = {(sr, sc, 0): energy}

        while q:
            r, c, m, e, d = q.popleft()
            if not e:
                continue
            for nr, nc in self._get_neighbors(r, c, R, C):
                val = classroom[nr][nc]
                if val == 'X':
                    continue
                ne = energy if val == 'R' else e - 1
                nm = m | (1 << ls[(nr, nc)]) if (nr, nc) in ls else m
                if nm == req:
                    return d + 1
                if ne > vis.get((nr, nc, nm), -1):
                    vis[(nr, nc, nm)] = ne
                    q.append((nr, nc, nm, ne, d + 1))
        return -1
