class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        str_s = {}
        total = 0
        for sc, c in zip(s, cost):
            total += c
            str_s[sc] = str_s.get(sc, 0) + c
        return total - max(str_s.values())

