class Solution:
    def largestMagicSquare(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [[0] * (n + 1) for _ in range(m)]
        cols = [[0] * (m + 1) for _ in range(n)]
        diag = [[0] * (n + 2) for _ in range(m + 1)]
        anti = [[0] * (n + 2) for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                rows[r][c+1] = rows[r][c] + grid[r][c]
                cols[c][r+1] = cols[c][r] + grid[r][c]
                diag[r+1][c+1] = diag[r][c] + grid[r][c]
                anti[r+1][c+1] = anti[r][c+2] + grid[r][c]

        def check(r, c, k):
            target = rows[r][c+k] - rows[r][c]
            for i in range(r + 1, r + k):
                if rows[i][c+k] - rows[i][c] != target: return False
            for j in range(c, c + k):
                if cols[j][r+k] - cols[j][r] != target: return False
            if diag[r+k][c+k] - diag[r][c] != target: return False
            if anti[r+k][c+1] - anti[r][c+k+1] != target: return False
            return True

        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if check(r, c, k):
                        return k
        return 1

