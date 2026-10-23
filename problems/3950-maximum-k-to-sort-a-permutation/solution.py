class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        misplaced = [x for i, x in enumerate(nums) if i != x]
        return reduce(and_, misplaced) if misplaced else 0
