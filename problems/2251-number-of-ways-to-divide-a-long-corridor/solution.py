class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9 + 7
        
        seats = [i for i, c in enumerate(corridor) if c == 'S']

        if not seats or len(seats) % 2 != 0:
            return 0

        res = 1
        
        for i in range(2, len(seats), 2):
            prev_end = seats[i - 1]
            curr_start = seats[i]
            
            ways_to_cut = curr_start - prev_end
            
            res = (res * ways_to_cut) % mod

        return res

