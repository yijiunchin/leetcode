class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        return [
            q for q in queries 
            if any(sum(x != y for x, y in zip(q, d)) <= 2 for d in dictionary)
        ]
