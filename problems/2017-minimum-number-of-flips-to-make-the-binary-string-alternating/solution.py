class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s2 = s + s
        ans = float('inf')
        d1 = d2 = 0
        
        for i, c in enumerate(s2):
            d1 += c != "01"[i % 2]
            d2 += c != "10"[i % 2]
            
            if i >= n:
                d1 -= s2[i - n] != "01"[(i - n) % 2]
                d2 -= s2[i - n] != "10"[(i - n) % 2]
                
            if i >= n - 1:
                ans = min(ans, d1, d2)
                
        return ans
