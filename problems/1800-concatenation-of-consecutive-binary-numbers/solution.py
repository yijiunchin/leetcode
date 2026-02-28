class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans, mod = 0, 10**9 + 7
        for i in range(1, n + 1):
            ans = ((ans << i.bit_length()) | i) % mod
        return ans
