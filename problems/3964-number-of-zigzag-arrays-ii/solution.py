class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        k, MOD = r - l + 1, 10**9 + 7
        
        def multiply(A, B):
            B_T = list(zip(*B))
            return [[sum(a * b for a, b in zip(row, col)) % MOD for col in B_T] for row in A]
        
        M = [[1 if i + j <= k - 2 else 0 for j in range(k)] for i in range(k)]
        res = [[1 if i == j else 0 for j in range(k)] for i in range(k)]
        
        p = n - 2
        while p:
            if p & 1:
                res = multiply(res, M)
            M = multiply(M, M)
            p >>= 1
            
        return sum(res[i][j] * (k - 1 - j) for i in range(k) for j in range(k)) * 2 % MOD
