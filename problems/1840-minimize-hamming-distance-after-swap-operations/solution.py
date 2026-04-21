class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        p = list(range(len(source)))
        
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
            
        for u, v in allowedSwaps:
            p[find(u)] = find(v)
            
        count = defaultdict(Counter)
        for i, val in enumerate(source):
            count[find(i)][val] += 1
            
        ans = 0
        for i, val in enumerate(target):
            root = find(i)
            if count[root][val] > 0:
                count[root][val] -= 1
            else:
                ans += 1
                
        return ans
