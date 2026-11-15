class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        ans = curr = 0
        cnt = [1, 0]
        for x in arr:
            curr ^= x & 1
            ans += cnt[1 ^ curr]
            cnt[curr] += 1
        return ans % 1_000_000_007
