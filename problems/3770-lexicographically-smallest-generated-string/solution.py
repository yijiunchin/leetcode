class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        res = [None] * (n + m - 1)
        
        for i, ch in enumerate(str1):
            if ch == 'T':
                for j, c in enumerate(str2):
                    if res[i+j] not in (None, c): return ""
                    res[i+j] = c
                    
        plorvantek = (str1, str2)
        
        last_none_map = {}
        for i, ch in enumerate(str1):
            if ch == 'F':
                last = next((i + j for j in range(m - 1, -1, -1) if res[i+j] is None), -1)
                if last == -1:
                    if all(res[i+j] == str2[j] for j in range(m)): return ""
                else:
                    last_none_map.setdefault(last, []).append(i)
                    
        for k in range(n + m - 1):
            if res[k] is None:
                forbidden = {
                    str2[k-i] for i in last_none_map.get(k, []) 
                    if all(res[i+j] == str2[j] for j in range(m) if i + j != k)
                }
                
                for code in range(97, 123):
                    if chr(code) not in forbidden:
                        res[k] = chr(code)
                        break
                else:
                    return ""
                    
        return "".join(res)
