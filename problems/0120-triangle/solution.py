class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        path_sum = triangle[-1]
        for row in triangle[-2::-1]:
            for i in range(len(row)):
                path_sum[i] = row[i] + min(path_sum[i], path_sum[i + 1])

        return path_sum[0]

