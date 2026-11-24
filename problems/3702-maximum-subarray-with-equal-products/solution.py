class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 2
        prod = 1
        left = 0
        for right, x in enumerate(nums):
            while gcd(prod, x) > 1:
                prod //= nums[left]
                left += 1
            prod *= x
            ans = max(ans, right - left + 1)
        return ans
