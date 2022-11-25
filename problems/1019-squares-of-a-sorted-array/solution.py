class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([value ** 2 for value in nums])
