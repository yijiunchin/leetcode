class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        masks = collections.defaultdict(int)
        for r, c in reservedSeats:
            masks[r] |= 1 << c
            
        ans = 2 * n
        for mask in masks.values():
            if not (mask & 60) and not (mask & 960):
                continue
            if not (mask & 60) or not (mask & 960) or not (mask & 240):
                ans -= 1
            else:
                ans -= 2
                
        return ans
