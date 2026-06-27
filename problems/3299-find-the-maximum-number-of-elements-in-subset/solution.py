class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = max(1, cnt[1] - (cnt[1] % 2 == 0))
        
        for x in cnt:
            if x > 1 and cnt[x] >= 2:
                cur = 0
                while cnt[x] >= 2:
                    cur += 2
                    x *= x
                ans = max(ans, cur + (1 if cnt[x] else -1))
                
        return ans
