class Solution:
    def isNumber(self, s: str) -> bool:
        
        try:
            if s in ('inf', '-inf', '+inf', 'Infinity', '+Infinity', '-Infinity', 'nan'): return False
            float(s)
            return True
        except:
            return False
