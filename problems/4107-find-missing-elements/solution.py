class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        max_n = max(nums)
        min_n = min(nums)
        ans = []
        for i in range(min_n + 1, max_n):
            if i not in nums:
                ans.append(i)
        return ans
        
