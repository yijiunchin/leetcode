class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 1e9 + 7
        pre_a = pre_b = 6
        for i in range(n - 1):
            tmp_a = (pre_a * 3 + pre_b * 2) % mod
            tmp_b = (pre_a * 2 + pre_b * 2) % mod
            pre_a = tmp_a
            pre_b = tmp_b
        return int((pre_a + pre_b) % mod)
