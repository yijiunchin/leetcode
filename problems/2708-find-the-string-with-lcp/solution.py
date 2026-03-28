class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        s = [''] * n
        c = 97
        for i in range(n):
            if not s[i]:
                if c > 122: return ''
                for j in range(i, n):
                    if lcp[i][j] and not s[j]:
                        s[j] = chr(c)
                c += 1
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                v = 1 + (lcp[i+1][j+1] if i + 1 < n and j + 1 < n else 0) if s[i] == s[j] else 0
                if lcp[i][j] != v: return ''
                
        return ''.join(s)
