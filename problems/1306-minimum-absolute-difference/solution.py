class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        pairs = []
        diff_min = -1
        for m, n in pairwise(sorted(arr)):
            diff = n - m
            if diff_min == -1 or diff < diff_min:
                pairs = [[m, n]]
                diff_min = diff
            elif diff == diff_min:
                pairs.append([m, n])

        return pairs

