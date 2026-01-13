class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        y_max = 0
        y_min = squares[0][1]
        total = 0

        for x, y, l in squares:
            total += l ** 2
            y_max = max(y_max, y + l)
            y_min = min(y_min, y)

        while abs(y_max - y_min) > 1e-5:
            mid = (y_max + y_min) / 2 
            if sum(l * min(mid - y, l) for x, y, l in squares if y < mid) >= total / 2:
                y_max = mid
            else:
                y_min = mid

        return y_max

