class Solution:
    def reverseByType(self, s: str) -> str:
        letters = []
        specials = []
        for c in s:
            if c in string.ascii_lowercase:
                letters.append(c)
            else:
                specials.append(c)

        ans = ''
        letters.reverse()
        specials.reverse()
        i = j = 0
        for c in s:
            if c in string.ascii_lowercase:
                ans += letters[i]
                i += 1
            else:
                ans += specials[j]
                j += 1
                
        return ans

