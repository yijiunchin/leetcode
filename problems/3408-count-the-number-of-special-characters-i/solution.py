class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        cnt = 0
        for i in range(26):
            if string.ascii_lowercase[i] in word and string.ascii_uppercase[i] in word:
               cnt += 1

        return cnt
