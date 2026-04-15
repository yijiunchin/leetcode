class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        return min((min(abs(i - startIndex), n - abs(i - startIndex)) 
                    for i, w in enumerate(words) if w == target), default=-1)
