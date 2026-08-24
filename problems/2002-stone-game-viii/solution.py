class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        p = list(accumulate(stones))
        return reduce(lambda ans, val: max(ans, val - ans), p[-2:0:-1], p[-1])
