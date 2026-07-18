class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(x, y):
            return x if y == 0 else gcd(y, x % y)

        return gcd(max(nums), min(nums))
