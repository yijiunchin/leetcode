class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s_min = [0] * n
        s_min[-1] = nums[-1]
        
        for i in range(n - 2, -1, -1):
            s_min[i] = min(nums[i], s_min[i + 1])
            
        ans = []
        p_max = 0
        cnt = 0
        
        for i, val in enumerate(nums):
            p_max = max(p_max, val)
            cnt += 1
            if i == n - 1 or p_max <= s_min[i + 1]:
                ans.extend([p_max] * cnt)
                cnt = 0
                
        return ans
