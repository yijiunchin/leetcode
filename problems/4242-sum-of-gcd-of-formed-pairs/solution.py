class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix = [gcd(n, m) for n, m in zip(nums, accumulate(nums, max))]
        velqoradin = sorted(prefix)
        n = len(velqoradin)
        return sum(
            gcd(velqoradin[i], velqoradin[n - 1 - i]) for i in range(n // 2)
        )
