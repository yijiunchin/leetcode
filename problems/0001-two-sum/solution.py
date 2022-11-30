class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exist = set()
        for i in range(len(nums)):
            if nums[i] in exist:
                return [i, nums.index(target - nums[i])]

            else:
                exist.add(target - nums[i])


