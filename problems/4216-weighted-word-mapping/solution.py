class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ''
        for s in words:
            ans += chr(122 - sum(weights[ord(c) - 97] for c in s) % 26)

        return ans
