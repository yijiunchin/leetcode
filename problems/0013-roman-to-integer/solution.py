class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        last = ''

        for i in s[::-1]:
            if i == 'I' and last in ('V', 'X'):
                ans -= 1
                continue
            if i == 'X' and last in ('L', 'C'):
                ans -= 10
                continue
            if i == 'C' and last in ('D', 'M'):
                ans -= 100
                continue
            if i == 'I': ans += 1
            elif i == 'V': ans += 5
            elif i == 'X': ans += 10
            elif i == 'L': ans += 50
            elif i == 'C': ans += 100
            elif i == 'D': ans += 500
            elif i == 'M': ans += 1000
            last = i

        return ans

