class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        sys.setrecursionlimit(max(sys.getrecursionlimit(), n + 100))
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)

        ans = [1] * n
        anc = {}

        def dfs(x: int) -> None:
            c = s[x]
            old = anc.get(c, -1)
            anc[c] = x
            for y in g[x]:
                dfs(y)
            anc[c] = old
            if x:
                ans[old if old != -1 else parent[x]] += ans[x]

        dfs(0)
        return ans
