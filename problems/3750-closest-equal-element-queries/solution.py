class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)
            
        n = len(nums)
        ans = [-1] * n
        
        for indices in pos.values():
            k = len(indices)
            if k > 1:
                for i in range(k):
                    ans[indices[i]] = min(
                        (indices[i] - indices[i - 1]) % n,
                        (indices[(i + 1) % k] - indices[i]) % n
                    )
                    
        return [ans[q] for q in queries]
