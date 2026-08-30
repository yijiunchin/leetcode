class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        i, j = sorted([nums.index(min(nums)), nums.index(max(nums))])
        return min(j + 1, len(nums) - i, i + 1 + len(nums) - j)
