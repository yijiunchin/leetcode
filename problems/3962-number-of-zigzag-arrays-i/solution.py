class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        if n == 1:
            return r - l + 1
        k, MOD = r - l + 1, 10**9 + 7
        U = D = [1] * k
        for _ in range(n - 1):
            U, D = [0] + [x % MOD for x in itertools.accumulate(D)][:-1], [x % MOD for x in itertools.accumulate(U[::-1])][:-1][::-1] + [0]
        return (sum(U) + sum(D)) % MOD
