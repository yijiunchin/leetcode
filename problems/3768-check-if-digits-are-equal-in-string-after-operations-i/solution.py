class Solution:
    def hasSameDigits(self, s: str) -> bool:

        while len(s) != 2:
            temp = ''
            for i in range(0, len(s) - 1):
                temp += str((int(s[i]) + int(s[i + 1])) % 10)
            s = temp
        if s[0] == s[1]: return True
        return False

