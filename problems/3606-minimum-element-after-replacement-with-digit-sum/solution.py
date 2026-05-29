class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = sum(int(n) for n in str(nums[i]))

        return min(nums)
