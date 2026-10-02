class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def dfs(l, r, s):
            if len(s) == n * 2:
                return [s]
            ans = dfs(l - 1, r, s + '(') if l else []
            ans += dfs(l, r - 1, s + ')') if r > l else []
            return ans

        return dfs(n, n, '')
