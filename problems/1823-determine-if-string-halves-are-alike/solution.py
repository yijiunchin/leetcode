class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a, b = 0, 0
        vowels = 'aeiouAEIOU'
        for i in vowels:
            a += s.count(i, 0, len(s) // 2)
            b += s.count(i, len(s) // 2)
            
        return a == b


