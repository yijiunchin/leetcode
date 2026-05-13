class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        diff = [0] * (2 * limit + 2)
        
        for a, b in zip(nums[:len(nums) // 2], reversed(nums)):
            lo, hi = min(a, b), max(a, b)
            
            diff[2] += 2
            diff[lo + 1] -= 1
            diff[lo + hi] -= 1
            diff[lo + hi + 1] += 1
            diff[hi + limit + 1] += 1
            
        ans = len(nums)
        curr = 0
        
        for i in range(2, 2 * limit + 1):
            curr += diff[i]
            if curr < ans:
                ans = curr
                
        return ans
