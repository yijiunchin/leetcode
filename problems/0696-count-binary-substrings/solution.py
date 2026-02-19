class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [len(list(g)) for _, g in itertools.groupby(s)]
        return sum(min(a, b) for a, b in zip(groups, groups[1:]))
