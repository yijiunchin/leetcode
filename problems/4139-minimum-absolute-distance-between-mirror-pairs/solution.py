class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        seen = {}
        ans = float('inf')
        
        for j, x in enumerate(nums):
            if x in seen:
                ans = min(ans, j - seen[x])
            seen[int(str(x)[::-1])] = j
            
        return ans if ans != float('inf') else -1
