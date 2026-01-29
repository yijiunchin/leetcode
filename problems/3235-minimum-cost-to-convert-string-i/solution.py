class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        inf = float('inf')
        min_costs = [[inf] * 26 for _ in range(26)]
        
        for i in range(26):
            min_costs[i][i] = 0
            
        for o, c, w in zip(original, changed, cost):
            u, v = ord(o) - 97, ord(c) - 97
            min_costs[u][v] = min(min_costs[u][v], w)
            
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    min_costs[i][j] = min(min_costs[i][j], min_costs[i][k] + min_costs[k][j])
                    
        total_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            
            u, v = ord(s) - 97, ord(t) - 97
            current_cost = min_costs[u][v]
            
            if current_cost == inf:
                return -1
            total_cost += current_cost
            
        return total_cost

