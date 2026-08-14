class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = l = 0
        cnt = {}
        for i, c in enumerate(s):
            cnt[c] = cnt.get(c, 0) + 1
            while cnt[c] > 2:
                cnt[s[l]] -= 1
                l += 1
            ans = max(ans, i - l + 1)

        return ans
