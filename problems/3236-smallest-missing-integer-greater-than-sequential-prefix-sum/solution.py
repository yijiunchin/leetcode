class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            i += 1
        ans = sum(nums[:i])
        num_set = set(nums)
        while ans in num_set:
            ans += 1
        return ans
