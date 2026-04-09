class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        groups = defaultdict(list)
        for l, r, k, v in queries:
            groups[k].append((l, r, v))
            
        for k, q_list in groups.items():
            total_steps = sum((r - l) // k + 1 for l, r, v in q_list)
            
            if total_steps < n:
                for l, r, v in q_list:
                    for i in range(l, r + 1, k):
                        nums[i] = (nums[i] * v) % MOD
            else:
                arr = [1] * n
                for l, r, v in q_list:
                    arr[l] = (arr[l] * v) % MOD
                    nxt = l + ((r - l) // k + 1) * k
                    if nxt < n:
                        arr[nxt] = (arr[nxt] * pow(v, MOD - 2, MOD)) % MOD
                        
                for i in range(k, n):
                    arr[i] = (arr[i] * arr[i - k]) % MOD
                    
                for i in range(n):
                    if arr[i] != 1:
                        nums[i] = (nums[i] * arr[i]) % MOD
                        
        return reduce(xor, nums)
