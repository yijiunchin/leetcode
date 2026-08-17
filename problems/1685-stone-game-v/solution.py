sys.setrecursionlimit(2000)


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        p = [0] + list(accumulate(stoneValue))
        
        @cache
        def dp(i, j):
            if i == j:
                return 0
            
            m = bisect_right(p, (p[i] + p[j + 1]) / 2, i + 1, j + 1) - 2
            
            res = max_l(i, m) if m >= i else 0
            
            if p[m + 1] * 2 == p[i] + p[j + 1]:
                res = max(res, max_r(m + 1, j))
            elif m + 2 <= j:
                res = max(res, max_r(m + 2, j))
                
            return res

        @cache
        def max_l(i, j):
            if i == j:
                return stoneValue[i]
            return max(max_l(i, j - 1), p[j + 1] - p[i] + dp(i, j))
            
        @cache
        def max_r(i, j):
            if i == j:
                return stoneValue[j]
            return max(max_r(i + 1, j), p[j + 1] - p[i] + dp(i, j))
        
        return dp(0, len(stoneValue) - 1)
