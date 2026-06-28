class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        res = 0
        for a in arr:
            res = min(res + 1, a)
        return res
