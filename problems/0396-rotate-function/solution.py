class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        s, n = sum(nums), len(nums)
        f = sum(i * v for i, v in enumerate(nums))
        ans = f
        
        for i in range(1, n):
            f += s - n * nums[-i]
            if f > ans:
                ans = f
                
        return ans
