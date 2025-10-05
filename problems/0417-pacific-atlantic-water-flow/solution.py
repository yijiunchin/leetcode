class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = []
        atlantic = []
        can_flow_pacific = set()
        can_flow_atlantic = set()

        m = len(heights)
        n = len(heights[0])

        for i in range(m):
            pacific.append((i, 0))
            atlantic.append((i, n - 1))
            can_flow_pacific.add((i, 0))
            can_flow_atlantic.add((i, n - 1))

        for i in range(n):
            pacific.append((0, i))
            atlantic.append((m - 1, i))
            can_flow_pacific.add((0, i))
            can_flow_atlantic.add((m - 1, i))

        while pacific:
            px, py = pacific.pop(0)
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                npx, npy = dx + px, dy + py
                if (
                    0 <= npx < m
                    and 0 <= npy < n
                    and (npx, npy) not in can_flow_pacific
                    and heights[px][py] <= heights[npx][npy]
                ):
                    can_flow_pacific.add((npx, npy))
                    pacific.append((npx, npy))

        while atlantic:
            ax, ay = atlantic.pop(0)
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nax, nay = dx + ax, dy + ay
                if (
                    0 <= nax < m
                    and 0 <= nay < n
                    and (nax, nay) not in can_flow_atlantic
                    and heights[ax][ay] <= heights[nax][nay]
                ):
                    can_flow_atlantic.add((nax, nay))
                    atlantic.append((nax, nay))

        return list(can_flow_pacific & can_flow_atlantic)

