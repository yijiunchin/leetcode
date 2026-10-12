class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        counts = [0] * 30
        for x in nums:
            for i in range(30):
                if (x >> i) & 1:
                    counts[i] += 1

        ans = 0
        mod = 1_000_000_007
        for _ in range(k):
            val = 0
            for i in range(30):
                if counts[i]:
                    val |= 1 << i
                    counts[i] -= 1
            ans = (ans + val**2) % mod

        return ans
