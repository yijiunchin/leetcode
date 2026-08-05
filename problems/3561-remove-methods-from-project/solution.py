class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)
        suspicious = {k}
        stack = [k]
        while stack:
            curr = stack.pop()
            for nxt in graph[curr]:
                if nxt not in suspicious:
                    suspicious.add(nxt)
                    stack.append(nxt)
        if any(u not in suspicious and v in suspicious for u, v in invocations):
            return list(range(n))
        return [i for i in range(n) if i not in suspicious]
