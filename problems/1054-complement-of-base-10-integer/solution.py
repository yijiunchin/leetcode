class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int(bin(n)[2:].replace('0', '2').replace('1', '0').replace('2', '1'), 2)
