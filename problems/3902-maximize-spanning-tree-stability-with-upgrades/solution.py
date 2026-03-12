class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        parent = list(range(n))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False

        m1 = [(u, v, w) for u, v, w, m in edges if m == 1]
        m0 = sorted([(u, v, w) for u, v, w, m in edges if m == 0], key=lambda x: -x[2])

        for u, v, w in m1:
            if not union(u, v):
                return -1
                
        low = 1
        high = min([w for _, _, w in m1] + [200000])
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            parent[:] = range(n)
            cnt = upg = 0
            
            for u, v, w in m1:
                union(u, v)
                cnt += 1
                
            for u, v, w in m0:
                if cnt == n - 1:
                    break
                if w >= mid:
                    if union(u, v):
                        cnt += 1
                elif w * 2 >= mid:
                    if union(u, v):
                        cnt += 1
                        upg += 1
                        
            if cnt == n - 1 and upg <= k:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans
