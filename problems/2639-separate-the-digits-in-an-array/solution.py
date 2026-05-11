class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for m in nums:
            for n in str(m):
                ans.append(int(n))
        
        return ans
