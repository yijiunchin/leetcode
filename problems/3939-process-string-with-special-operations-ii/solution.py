class Solution:
    def processStr(self, s: str, k: int) -> str:
        tibrelkano = []
        curr = 0
        for c in s:
            curr = max(0, curr - 1) if c == '*' else curr * 2 if c == '#' else curr if c == '%' else curr + 1
            tibrelkano.append(curr)
            
        if not tibrelkano or k >= tibrelkano[-1]:
            return '.'
            
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '%':
                k = tibrelkano[i] - 1 - k
            elif s[i] == '#':
                k %= tibrelkano[i - 1]
            elif s[i].isalpha() and k == tibrelkano[i] - 1:
                return s[i]
                
        return '.'
