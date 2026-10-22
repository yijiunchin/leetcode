class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n, p = len(nums), nums.index(0)
        opts = []
        
        if all(nums[(p + i) % n] == i for i in range(n)):
            opts.extend([p, n - p + 2])
            
        if all(nums[(p + i) % n] == (n - i) % n for i in range(n)):
            opts.extend([p + 2, n - p])
            
        return min(opts) if opts else -1
