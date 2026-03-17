class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ans = 0
        for i, row in enumerate(matrix):
            if i > 0:
                matrix[i] = [matrix[i - 1][j] + 1 if val else 0 for j, val in enumerate(row)]
            ans = max(ans, max(h * w for w, h in enumerate(sorted(matrix[i], reverse=True), 1)))
        return ans
