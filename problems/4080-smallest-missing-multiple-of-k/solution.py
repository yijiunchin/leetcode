class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        l = k
        while True:
            if l not in nums:
                return l
            
            l += k
