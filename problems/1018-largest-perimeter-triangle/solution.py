class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        largest_perimeter = 0
        nums = sorted(nums)
        for i in range(len(nums) - 1, 1, -1):
            if nums[i - 2] + nums[i - 1] > nums[i]:
                largest_perimeter = max(largest_perimeter, nums[i - 2] + nums[i - 1] + nums[i])

        return largest_perimeter

