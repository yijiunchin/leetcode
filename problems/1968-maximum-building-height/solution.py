class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.extend([[1, 0], [n, n - 1]])
        restrictions.sort()
        m = len(restrictions)
        
        for i in range(1, m):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1] + restrictions[i][0] - restrictions[i-1][0])
            
        for i in range(m - 2, -1, -1):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + restrictions[i+1][0] - restrictions[i][0])
            
        return max((r[0] - l[0] + l[1] + r[1]) // 2 for l, r in zip(restrictions, restrictions[1:]))
