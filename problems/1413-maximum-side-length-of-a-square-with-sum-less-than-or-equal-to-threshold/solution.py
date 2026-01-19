class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre[i][j] = (pre[i-1][j] + pre[i][j-1] - 
                             pre[i-1][j-1] + mat[i-1][j-1])
        
        def get_sum(r1, c1, r2, c2):
            return pre[r2][c2] - pre[r1-1][c2] - pre[r2][c1-1] + pre[r1-1][c1-1]

        ans = 0
        k = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                while (i + k - 1 <= m and j + k - 1 <= n and 
                       get_sum(i, j, i + k - 1, j + k - 1) <= threshold):
                    ans = k
                    k += 1
        return ans

