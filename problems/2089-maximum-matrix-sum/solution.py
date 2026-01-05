class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        total = count = 0
        min_abs = float('inf')

        for row in matrix:
            for n in row:
                total += abs(n)
                if n < 0:
                    count += 1
                if abs(n) < min_abs:
                    min_abs = abs(n)

        if count % 2 == 0:
            return total
        return total - 2 * min_abs

