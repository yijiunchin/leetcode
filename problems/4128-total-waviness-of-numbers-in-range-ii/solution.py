class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(num):
            s = str(num)
            
            @cache
            def dfs(i, p1, p2, is_limit, is_num):
                if i == len(s): 
                    return 0, 1
                
                res_f = res_c = 0
                up = int(s[i]) if is_limit else 9
                
                for d in range(up + 1):
                    nxt_lim = is_limit and d == up
                    if not is_num:
                        f, c = dfs(i + 1, d if d else -1, -1, nxt_lim, d > 0)
                    else:
                        f, c = dfs(i + 1, d, p1, nxt_lim, True)
                        if p2 != -1 and (p2 < p1 > d or p2 > p1 < d):
                            f += c
                    res_f += f
                    res_c += c
                    
                return res_f, res_c
            
            return dfs(0, -1, -1, True, False)[0]
        
        return solve(num2) - solve(num1 - 1)
