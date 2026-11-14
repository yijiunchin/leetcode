class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        return min(
            (
                s
                for i in range(len(nums))
                for j in range(i + l, i + r + 1)
                if j <= len(nums) and (s := sum(nums[i:j])) > 0
            ),
            default=-1,
        )
