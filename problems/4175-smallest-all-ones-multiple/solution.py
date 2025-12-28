class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0: return -1
        remainder = 1 % k
        l = 1
        while remainder != 0:
            remainder = (remainder * 10 + 1) % k
            l += 1
        return l

