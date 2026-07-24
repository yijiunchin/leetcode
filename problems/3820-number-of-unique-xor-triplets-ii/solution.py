class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        s = set(nums)
        return len({x ^ y for x in {a ^ b for a in s for b in s} for y in s})
