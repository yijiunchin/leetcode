class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = inc = dec = 1
        for a, b in zip(nums, nums[1:]):
            inc = inc + 1 if b > a else 1
            dec = dec + 1 if b < a else 1
            ans = max(ans, inc, dec)
        return ans
