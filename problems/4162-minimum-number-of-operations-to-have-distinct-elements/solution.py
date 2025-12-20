class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = set()
        n = len(nums)

        for i in range(n - 1, -1, -1):
            if nums[i] in s:
                return (i + 1 + 2) // 3
            s.add(nums[i])

        return 0

