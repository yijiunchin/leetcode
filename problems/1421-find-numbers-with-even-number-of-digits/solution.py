class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([integers for integers in nums if len(str(integers)) % 2 == 0])
