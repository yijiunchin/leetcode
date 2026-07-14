class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        dp = {(0, 0): 1}
        mod = 10**9 + 7
        for x in nums:
            nxt = dict(dp)
            for (g1, g2), cnt in dp.items():
                n1, n2 = gcd(g1, x), gcd(g2, x)
                nxt[(n1, g2)] = (nxt.get((n1, g2), 0) + cnt) % mod
                nxt[(g1, n2)] = (nxt.get((g1, n2), 0) + cnt) % mod
            dp = nxt
        return sum(c for (g1, g2), c in dp.items() if g1 == g2 and g1) % mod
