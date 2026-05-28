class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = {}
        for i, w in enumerate(wordsContainer):
            curr = trie
            for c in w[::-1] + " ":
                if '$' not in curr or (len(w), i) < (len(wordsContainer[curr['$']]), curr['$']):
                    curr['$'] = i
                if c != " ":
                    curr = curr.setdefault(c, {})
        
        ans = []
        for q in wordsQuery:
            curr = trie
            for c in q[::-1]:
                if c not in curr:
                    break
                curr = curr[c]
            ans.append(curr['$'])
        return ans
