class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive = 0
        maxconsecutive = 0
        for i in nums:
            if i == 1:
                consecutive += 1

            elif i == 0:
                consecutive = 0

            if consecutive >= maxconsecutive:
                maxconsecutive = consecutive

        return maxconsecutive
