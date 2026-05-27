class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}
        
        for i, char in enumerate(word):
            if char.islower():
                last_lower[char] = i
            elif char not in first_upper:
                first_upper[char] = i
                
        ans = 0
        for char, lower_idx in last_lower.items():
            upper_char = char.upper()
            if upper_char in first_upper and lower_idx < first_upper[upper_char]:
                ans += 1
                
        return ans
