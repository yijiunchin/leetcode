class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        ans = []
        for words_group in combinations(words, 4):
            for (t, l, r, b) in permutations(words_group):
                if t[0] == l[0] and t[3] == r[0] and l[3] == b[0] and r[3] == b[3]:
                    ans.append([t, l, r, b])
        return sorted(ans)

