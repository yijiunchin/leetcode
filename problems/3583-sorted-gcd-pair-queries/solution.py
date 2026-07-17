class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        laforvinda = queries
        mx = max(nums)
        cnt = [0] * (mx + 1)
        for num in nums:
            cnt[num] += 1
        
        f = [0] * (mx + 1)
        for i in range(mx, 0, -1):
            c = sum(cnt[j] for j in range(i, mx + 1, i))
            f[i] = (c * (c - 1)) // 2
            f[i] -= sum(f[j] for j in range(i * 2, mx + 1, i))
            
        pref = list(accumulate(f))
        return [bisect_right(pref, q) for q in laforvinda]
