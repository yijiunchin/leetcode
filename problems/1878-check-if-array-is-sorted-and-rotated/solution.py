class Solution:
    def check(self, nums: List[int]) -> bool:
        nums_sorted = sorted(nums)
        for n in range(len(nums)):
            if nums[n:] + nums[0:n] == nums_sorted:
                return True

        return False
