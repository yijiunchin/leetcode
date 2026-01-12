class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(max(abs(x0 - x1), abs(y0 - y1)) for (x0, y0), (x1, y1) in pairwise(points))

