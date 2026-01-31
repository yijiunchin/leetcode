class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        max_len  = 0
        for i in range(31):
            tails = []
            for n in nums:
                if (n >> i) & 1:
                    if not tails or n > tails[-1]:
                        tails.append(n)
                    else:
                        tails[bisect_left(tails, n)] = n

            max_len = max(max_len, len(tails))

        return max_len

