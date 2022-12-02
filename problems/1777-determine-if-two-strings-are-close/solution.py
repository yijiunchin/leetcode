class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_sort = sorted(Counter(word1).values())
        word2_sort = sorted(Counter(word2).values())

        word1_dict = set(word1)
        word2_dict = set(word2)

        return word1_sort == word2_sort and word1_dict == word2_dict
