class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = [words[0]]
        for i in range(1, len(words)):
            if ''.join(sorted(words[i])) == ''.join(sorted(words[i - 1])): continue
            ans.append(words[i])

        return ans

