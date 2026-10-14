class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ''
        q, r = divmod(sum, 9)
        return ('9' * q + str(r) + '0' * (num - q))[:num]
