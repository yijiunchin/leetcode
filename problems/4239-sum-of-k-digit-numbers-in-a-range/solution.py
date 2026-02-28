class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        digit_sum = (l + r) * m // 2
        
        term1 = digit_sum * pow(m, k - 1, MOD) % MOD
        term2 = (pow(10, k, MOD) - 1) * pow(9, -1, MOD) % MOD
        
        return (term1 * term2) % MOD
