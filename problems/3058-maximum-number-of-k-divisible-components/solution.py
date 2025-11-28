class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)
        result = 0
        def dfs(node, parent):
            nonlocal k, result
            val_sum = 0
            for next_node in adj_list[node]:
                if next_node != parent:
                    val_sum += dfs(next_node, node)
                    val_sum %= k
            val_sum += values[node]
            val_sum %= k
            if val_sum == 0:
                result += 1    
            return val_sum
        dfs(0, -1)
        return result
