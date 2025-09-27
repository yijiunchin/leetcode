class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0.0
        for p1, p2, p3 in itertools.combinations(points, 3):
            area = 0.5 * abs(
                p1[0] * (p2[1] - p3[1])
                + p2[0] * (p3[1] - p1[1])
                + p3[0] * (p1[1] - p2[1])
            )
            max_area = max(max_area, area)

        return max_area

