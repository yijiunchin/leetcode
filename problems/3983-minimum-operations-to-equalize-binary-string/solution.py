class Solution:
    def minOperations(self, s: str, k: int) -> int:
        c0 = s.count('0')
        c1 = len(s) - c0
        n = len(s)
        
        if k % 2 == 0 and c0 % 2 != 0:
            return -1
            
        for m in range(n + 2):
            if (m * k) % 2 == c0 % 2 and m * k >= c0:
                max_flips = (m - 1) * c0 + m * c1 if m % 2 == 0 else m * c0 + (m - 1) * c1
                if m * k <= max_flips:
                    return m
                    
        return -1
