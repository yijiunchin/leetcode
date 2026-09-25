class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        res = set()

        def dfs(exp: str) -> None:
            if '{' not in exp:
                res.add(exp)
                return
            r = exp.find('}')
            l = exp.rfind('{', 0, r)
            for part in exp[l + 1:r].split(','):
                dfs(exp[:l] + part + exp[r + 1:])

        dfs(expression)
        return sorted(res)
