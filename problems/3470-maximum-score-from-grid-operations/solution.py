class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        S = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                S[j][i + 1] = S[j][i] + grid[i][j]
        NEG = float('-inf')
        f = [[NEG] * (n + 1) for _ in range(n + 1)]
        for b in range(n + 1):
            f[0][b] = 0
        for j in range(n - 1):
            new_f = [[NEG] * (n + 1) for _ in range(n + 1)]
            for b in range(n + 1):
                P = [NEG] * (n + 2)
                for c in range(1, n + 2):
                    P[c] = max(P[c - 1], f[c - 1][b])
                Q = [NEG] * (n + 2)
                for c in range(n, -1, -1):
                    val = f[c][b]
                    if val != NEG:
                        diff = S[j][c] - S[j][b]
                        if diff > 0:
                            val = val + diff
                    Q[c] = max(Q[c + 1], val)
                for c in range(n + 1):
                    p_term = P[c]
                    if p_term != NEG:
                        diff = S[j][c] - S[j][b]
                        if diff > 0:
                            p_term = p_term + diff
                    q_term = Q[c]
                    new_f[b][c] = max(p_term, q_term)
            f = new_f
        ans = 0
        for a in range(n + 1):
            for b in range(n + 1):
                if f[a][b] == NEG:
                    continue
                diff = S[n - 1][a] - S[n - 1][b]
                if diff < 0:
                    diff = 0
                if f[a][b] + diff > ans:
                    ans = f[a][b] + diff
        return ans
