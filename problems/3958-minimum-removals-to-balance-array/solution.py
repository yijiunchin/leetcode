class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, max_len = 0, 0
        for right, val in enumerate(nums):
            while val > nums[left] * k:
                left += 1
            max_len = max(max_len, right - left + 1)
        return len(nums) - max_len
