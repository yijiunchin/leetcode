class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        pre = total = r1 = r2 = 0
        for n, c in zip(nums, colors):
            if c != pre:
                total += r2
                r1 = r2 = 0
                pre = c

            r1, r2 = r2, max(r2, r1 + n)

        return total + r2
