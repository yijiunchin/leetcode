class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        for s in zip(*strs):
            if len(set(s)) != 1:
                break
            ans += s[0]
        return ans

