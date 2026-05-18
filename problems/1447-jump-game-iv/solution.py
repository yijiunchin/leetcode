class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
            
        idx_map = {}
        for i, v in enumerate(arr):
            idx_map.setdefault(v, []).append(i)
            
        q, vis = [0], {0}
        step = 0
        
        while q:
            nxt = []
            for i in q:
                if i == n - 1:
                    return step
                    
                for j in idx_map.pop(arr[i], []) + [i - 1, i + 1]:
                    if 0 <= j < n and j not in vis:
                        vis.add(j)
                        nxt.append(j)
            q = nxt
            step += 1
            
        return step
