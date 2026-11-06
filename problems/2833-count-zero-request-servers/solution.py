class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda item: item[1])
        sorted_q = sorted(enumerate(queries), key=lambda item: item[1])
        ans = [0] * len(queries)
        freq = [0] * (n + 1)
        l = r = active = 0

        for i, q in sorted_q:
            while r < len(logs) and logs[r][1] <= q:
                srv = logs[r][0]
                if freq[srv] == 0:
                    active += 1
                freq[srv] += 1
                r += 1
            
            while l < len(logs) and logs[l][1] < q - x:
                srv = logs[l][0]
                freq[srv] -= 1
                if freq[srv] == 0:
                    active -= 1
                l += 1
            
            ans[i] = n - active

        return ans
