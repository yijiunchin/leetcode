class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = sorted(v for r in grid for v in r)
        if len(set(v % x for v in nums)) > 1:
            return -1
        mid = nums[len(nums) // 2]
        return sum(abs(v - mid) // x for v in nums)
