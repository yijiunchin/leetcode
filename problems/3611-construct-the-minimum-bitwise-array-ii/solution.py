class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        ans = []
        for n in nums:
            if n == 2:
                ans.append(-1)
                continue
            
            target_bit = (~n & (n + 1)) >> 1
            ans.append(n ^ target_bit)
            
        return ans

