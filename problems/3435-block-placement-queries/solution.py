class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        n = 50005
        tree = [0] * (2 * n)
        
        def update(i, val):
            i += n
            tree[i] = val
            i >>= 1
            while i:
                tree[i] = max(tree[i << 1], tree[i << 1 | 1])
                i >>= 1
                
        def query(r):
            res, l = 0, n
            r += n
            while l < r:
                if l & 1:
                    res = max(res, tree[l])
                    l += 1
                if r & 1:
                    r -= 1
                    res = max(res, tree[r])
                l >>= 1
                r >>= 1
            return res

        sl = SortedList([0])
        ans = []
        
        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = sl.bisect_left(x)
                update(x, x - sl[idx - 1])
                if idx < len(sl):
                    update(sl[idx], sl[idx] - x)
                sl.add(x)
            else:
                x, sz = q[1], q[2]
                last = sl[sl.bisect_right(x) - 1]
                ans.append(query(last + 1) >= sz or x - last >= sz)
                
        return ans
