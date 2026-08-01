class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = sorted(Counter(word).values(), reverse=True)
        return sum(count * ((i // 8) + 1) for i, count in enumerate(freq))
