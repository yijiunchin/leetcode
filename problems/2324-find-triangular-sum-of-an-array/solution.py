class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            new_nums = []
            for j in range(len(nums) - 1):
                new_nums.append((nums[j] + nums[j + 1]) % 10)
            nums = new_nums
        return nums[0]

