class Solution:
    def removeZeros(self, n: int) -> int:
        return int(''.join(str(n).split('0')))
