class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        return len(nums) > 1 and nums[-1] == nums[-2] and nums[:-1] == list(range(1, nums[-1] + 1))

