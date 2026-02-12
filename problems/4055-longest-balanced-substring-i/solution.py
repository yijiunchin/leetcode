class Solution:
    def longestBalanced(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            cnt = [0] * 26
            max_freq = distinct = 0
            for j in range(i, len(s)):
                idx = ord(s[j]) - 97
                if cnt[idx] == 0:
                    distinct += 1

                cnt[idx] += 1
                max_freq = max(max_freq, cnt[idx])
                if max_freq * distinct == j - i + 1:
                    ans = max(ans, j - i + 1)

        return ans
