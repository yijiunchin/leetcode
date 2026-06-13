class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ''
        for s in words:
            n = 0
            for c in s:
                n += weights[ord(c) - 97]

            ans += chr(122 - n % 26)

        return ans
