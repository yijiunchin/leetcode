class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        rob_set = set(robots)
        base_walls = len(rob_set.intersection(walls))
        vw = sorted(set(walls) - rob_set)
        
        def cnt(low, high):
            return bisect_right(vw, high) - bisect_left(vw, low) if low <= high else 0

        rds = sorted(zip(robots, distance))
        
        p_L = cnt(rds[0][0] - rds[0][1], rds[0][0] - 1)
        p_R = 0
        
        for i in range(1, len(rds)):
            x_p, d_p = rds[i-1]
            x_c, d_c = rds[i]
            
            rp = min(x_c, x_p + d_p)
            lc = max(x_p, x_c - d_c)
            
            g_LL = cnt(lc, x_c - 1)
            g_RL = cnt(x_p + 1, rp) + cnt(lc, x_c - 1) if rp < lc else cnt(x_p + 1, x_c - 1)
            g_RR = cnt(x_p + 1, rp)
            
            p_L, p_R = max(p_L + g_LL, p_R + g_RL), max(p_L, p_R + g_RR)
            
        return base_walls + max(p_L, p_R + cnt(rds[-1][0] + 1, rds[-1][0] + rds[-1][1]))
