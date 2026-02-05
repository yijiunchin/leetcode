class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        return [nums[(i + n) % len(nums)] for i, n in enumerate(nums)]
