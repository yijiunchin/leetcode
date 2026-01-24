class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        return max([m + n for m, n in zip(sorted(nums)[:len(nums) // 2], sorted(nums)[-1:len(nums) // 2 - 1: -1])])

