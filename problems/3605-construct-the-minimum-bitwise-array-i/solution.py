class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        ans = []
        for n in nums:
            if n == 2:
                ans.append(-1)
                continue
            
            for i in range(1, 32):
                if not (n & (1 << i)):
                    ans.append(n ^ (1 << (i - 1)))
                    break
        return ans

