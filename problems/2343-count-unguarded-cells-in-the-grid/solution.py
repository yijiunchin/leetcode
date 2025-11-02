class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def inRange(x, y) -> bool:
            return 0 <= x < m and 0 <= y < n

        # 0 default
        # 1 guarded
        # 2 guard/wall

        # Right, Down, Left, Up
        direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        grid = [[0] * n for _ in range(m)]
        q = deque()
        for x, y in walls:
            grid[x][y] = 2

        for x, y in guards:
            grid[x][y] = 2
            for i in range(4):
                if inRange(x + direc[i][0], y + direc[i][1]):
                    q.append((x + direc[i][0], y + direc[i][1], i))

        while q:
            x, y, d = q.popleft()
            if grid[x][y] == 2: continue
            grid[x][y] = 1

            if inRange(x + direc[d][0], y + direc[d][1]):
                q.append((x + direc[d][0], y + direc[d][1], d))

        return sum(i.count(0) for i in grid)
