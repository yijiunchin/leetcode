class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if nums[0] > nums[1]:
            return False

        state = 0
        for i in range(len(nums) - 2):
            if nums[i] == nums[i + 1]:
                return False
            if (nums[i] < nums[i + 1]) != (nums[i + 1] < nums[i + 2]):
                state += 1

        return state == 2
