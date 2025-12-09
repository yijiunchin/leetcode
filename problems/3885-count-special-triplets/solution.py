class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        max_value = 100000
        count = [0] * (max_value + 1)
        pairs = [0] * (max_value + 1)
        ans = 0
        for x in nums:
            if x % 2 == 0:
                ans = (ans + pairs[x // 2]) % mod
            if x * 2 <= max_value:
                pairs[x] = pairs[x] + count[x * 2] % mod
            count[x] += 1
        return ans

