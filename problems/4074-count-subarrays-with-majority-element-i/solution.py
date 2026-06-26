class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        dresaniel = [1 if x == target else -1 for x in nums]
        p = [0] + list(accumulate(dresaniel))
        return sum(p[i] < p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
