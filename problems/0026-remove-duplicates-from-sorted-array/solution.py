class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == last:
                del nums[i]
            
            else:
                last = nums[i]
