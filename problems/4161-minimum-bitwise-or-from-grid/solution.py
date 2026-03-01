class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        ans = 0
        for b in range(29, -1, -1):
            mask = ans | ((1 << b) - 1)
            if any(all(x & ~ mask for x in row) for row in grid):
                ans |= 1 << b

        return ans
