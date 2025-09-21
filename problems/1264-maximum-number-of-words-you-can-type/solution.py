class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        for word in text.split():
            count += all(char not in brokenLetters for char in word)
        return count

