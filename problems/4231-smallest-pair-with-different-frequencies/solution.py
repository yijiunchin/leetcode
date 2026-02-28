class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        counts = Counter(nums)
        for x, y in combinations(sorted(counts), 2):
            if counts[x] != counts[y]:
                return [x, y]
        return [-1, -1]
