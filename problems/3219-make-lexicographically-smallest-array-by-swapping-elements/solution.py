class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        ans = [0] * len(nums)
        pairs = sorted((x, i) for i, x in enumerate(nums))
        i = 0
        while i < len(pairs):
            j = i + 1
            while j < len(pairs) and pairs[j][0] - pairs[j - 1][0] <= limit:
                j += 1
            idx_group = sorted(p[1] for p in pairs[i:j])
            for idx, (val, _) in zip(idx_group, pairs[i:j]):
                ans[idx] = val
            i = j
        return ans
