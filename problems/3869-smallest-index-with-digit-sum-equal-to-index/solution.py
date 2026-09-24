class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            total = 0
            for m in list(str(n)):
                total += int(m)
            
            if total == i:
                return i

        return -1

