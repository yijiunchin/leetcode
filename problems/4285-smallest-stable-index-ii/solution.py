class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        p_max = accumulate(nums, max)
        s_min = list(accumulate(nums[::-1], min))[::-1]
        
        for i, (p, s) in enumerate(zip(p_max, s_min)):
            if p - s <= k:
                return i
        return -1
