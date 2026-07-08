class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        val = [0] * (n + 1)
        cnt = [0] * (n + 1)
        S = [0] * (n + 1)
        p10 = [1] * (n + 1)
        
        for i, char in enumerate(s):
            d = int(char)
            p10[i + 1] = (p10[i] * 10) % MOD
            if d > 0:
                val[i + 1] = (val[i] * 10 + d) % MOD
                cnt[i + 1] = cnt[i] + 1
                S[i + 1] = S[i] + d
            else:
                val[i + 1] = val[i]
                cnt[i + 1] = cnt[i]
                S[i + 1] = S[i]
                
        return [
            ((val[r + 1] - val[l] * p10[cnt[r + 1] - cnt[l]]) % MOD * (S[r + 1] - S[l])) % MOD 
            for l, r in queries
        ]
