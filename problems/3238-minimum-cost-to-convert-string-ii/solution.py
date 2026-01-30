class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        import math

        sub_to_id = {}
        next_id = 0
        for s in original:
            if s not in sub_to_id:
                sub_to_id[s] = next_id
                next_id += 1
        for s in changed:
            if s not in sub_to_id:
                sub_to_id[s] = next_id
                next_id += 1
        
        count = next_id
        inf = math.inf
        dist = [[inf] * count for _ in range(count)]
        for i in range(count):
            dist[i][i] = 0
            
        for u, v, w in zip(original, changed, cost):
            uid, vid = sub_to_id[u], sub_to_id[v]
            dist[uid][vid] = min(dist[uid][vid], w)
            
        for k in range(count):
            for i in range(count):
                if dist[i][k] == inf: continue
                for j in range(count):
                    if dist[k][j] != inf:
                        new_dist = dist[i][k] + dist[k][j]
                        if new_dist < dist[i][j]:
                            dist[i][j] = new_dist

        n = len(source)
        dp = [inf] * (n + 1)
        dp[0] = 0
        
        sizes = sorted(list(set(len(s) for s in original)))
        
        for i in range(n):
            if dp[i] == inf:
                continue
            
            if source[i] == target[i]:
                if dp[i] < dp[i+1]:
                    dp[i+1] = dp[i]
            
            for length in sizes:
                j = i + length
                if j > n:
                    break
                
                sub_s = source[i:j]
                sub_t = target[i:j]
                
                if sub_s in sub_to_id and sub_t in sub_to_id:
                    uid = sub_to_id[sub_s]
                    vid = sub_to_id[sub_t]
                    if dist[uid][vid] != inf:
                        if dp[i] + dist[uid][vid] < dp[j]:
                            dp[j] = dp[i] + dist[uid][vid]

        return dp[n] if dp[n] != inf else -1

