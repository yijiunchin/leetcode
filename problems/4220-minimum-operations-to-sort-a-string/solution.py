class Solution:
    def minOperations(self, s: str) -> int:
        if s == "".join(sorted(s)):
            return 0
        if len(s) < 3:
            return -1
        
        min_s, max_s = min(s), max(s)
        
        if s[0] == min_s or s[-1] == max_s:
            return 1
        if s[0] == max_s and s[-1] == min_s and s.count(max_s) == 1 and s.count(min_s) == 1:
            return 3
            
        return 2
