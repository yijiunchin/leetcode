class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) / 2
        s = set(nums)
        for num in nums:
            if nums.count(num) == n:
                return num

