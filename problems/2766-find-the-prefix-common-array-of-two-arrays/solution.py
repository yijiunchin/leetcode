class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()
        ans = []
        curr = 0
        for a, b in zip(A, B):
            curr += a in seen
            seen.add(a)
            curr += b in seen
            seen.add(b)
            ans.append(curr)
        return ans
