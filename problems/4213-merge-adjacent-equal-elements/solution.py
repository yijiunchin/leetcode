class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        s = []
        for n in nums:
            while s and s[-1] == n:
                n += s.pop()
            s.append(n)

        return s
