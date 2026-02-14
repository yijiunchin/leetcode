class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        counts = Counter(w[:k] for w in words if len(w) >= k)
        return sum(count >= 2 for count in counts.values())
