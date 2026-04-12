class Solution:
    def minimumDistance(self, word: str) -> int:
        def d(a, b):
            return 0 if a == 26 else abs(a // 6 - b // 6) + abs(a % 6 - b % 6)
        
        nums = [ord(c) - 65 for c in word]
        dp = [0] * 27
        
        for b, c in zip(nums, nums[1:]):
            dp[b] = max(dp[b], max(dp[a] + d(b, c) - d(a, c) for a in range(27)))
            
        return sum(d(x, y) for x, y in zip(nums, nums[1:])) - max(dp)
