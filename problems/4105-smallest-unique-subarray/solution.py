class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        mod = (1 << 61) - 1
        base = random.randint(100007, 10**9)
        h = [0] * (n + 1)
        p = [1] * (n + 1)
        for i, x in enumerate(nums):
            h[i + 1] = (h[i] * base + x) % mod
            p[i + 1] = (p[i] * base) % mod

        def has_unique(length: int) -> bool:
            pw = p[length]
            cnt = Counter(
                (h[i + length] - h[i] * pw) % mod
                for i in range(n - length + 1)
            )
            return 1 in cnt.values()

        return bisect_left(range(1, n + 1), True, key=has_unique) + 1
