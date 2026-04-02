class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        n = len(coins[0])
        MIN = -float('inf')
        dp = [[MIN] * 3 for _ in range(n)]
        
        for r, row in enumerate(coins):
            for c, v in enumerate(row):
                if r == 0 and c == 0:
                    dp[0] = [v, max(v, 0), max(v, 0)]
                    continue
                    
                t = dp[c]
                l = dp[c-1] if c > 0 else [MIN, MIN, MIN]
                
                m0 = max(t[0], l[0])
                m1 = max(t[1], l[1])
                m2 = max(t[2], l[2])
                
                dp[c] = [
                    m0 + v,
                    max(m1 + v, m0 if v < 0 else MIN),
                    max(m2 + v, m1 if v < 0 else MIN)
                ]
                
        return dp[-1][2]
