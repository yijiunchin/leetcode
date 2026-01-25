class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        last = nums[-1]
        i = 0
        for n in nums[-2::-1]:
            if n < last:
                i += 1
            else:
                return len(nums) - i - 1
            last = n
        return 0

