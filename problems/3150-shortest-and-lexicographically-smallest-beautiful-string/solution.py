class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        subs = [
            s[i:j]
            for i in range(len(s))
            for j in range(i + k, len(s) + 1)
            if s[i:j].count('1') == k
        ]
        return min(subs, key=lambda x: (len(x), x), default='')
