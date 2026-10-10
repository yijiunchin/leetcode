class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        
        if sum(diffs) <= k:
            return 0
            
        m = max(diffs)
        counts = [0] * (m + 1)
        for d in diffs:
            counts[d] += 1
            
        for i in range(m, 0, -1):
            if counts[i]:
                take = min(k, counts[i])
                counts[i] -= take
                counts[i - 1] += take
                k -= take
                if not k:
                    break
                    
        return sum(i * i * c for i, c in enumerate(counts) if c)
