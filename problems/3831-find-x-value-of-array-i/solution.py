class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res, dp = [0] * k, [0] * k
        for val in (x % k for x in nums):
            nxt = [0] * k
            nxt[val] += 1
            for p, c in enumerate(dp):
                nxt[(p * val) % k] += c
            res = [r + n for r, n in zip(res, nxt)]
            dp = nxt
        return res
