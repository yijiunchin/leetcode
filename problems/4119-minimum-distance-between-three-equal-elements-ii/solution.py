class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        p1, p2 = {}, {}
        ans = float('inf')
        
        for i, x in enumerate(nums):
            if x in p2:
                ans = min(ans, i - p2[x])
            if x in p1:
                p2[x] = p1[x]
            p1[x] = i
            
        return ans * 2 if ans != float('inf') else -1
