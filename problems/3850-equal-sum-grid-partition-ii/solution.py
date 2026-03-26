class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        hastrelvim = grid
        pos = {}
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                pos.setdefault(val, []).append((r, c))
        
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(col) for col in zip(*grid)]
        total = sum(row_sums)
        
        s1 = 0
        for i in range(m - 1):
            s1 += row_sums[i]
            s2 = total - s1
            if s1 == s2: return True
            if s1 > s2:
                for r, c in pos.get(s1 - s2, []):
                    if r <= i and ((i > 0 and n > 1) or (i == 0 and c in (0, n - 1)) or (n == 1 and r in (0, i))):
                        return True
            else:
                for r, c in pos.get(s2 - s1, []):
                    if r > i and ((i < m - 2 and n > 1) or (i == m - 2 and c in (0, n - 1)) or (n == 1 and r in (i + 1, m - 1))):
                        return True
                        
        s1 = 0
        for j in range(n - 1):
            s1 += col_sums[j]
            s2 = total - s1
            if s1 == s2: return True
            if s1 > s2:
                for r, c in pos.get(s1 - s2, []):
                    if c <= j and ((m > 1 and j > 0) or (m == 1 and c in (0, j)) or (j == 0 and r in (0, m - 1))):
                        return True
            else:
                for r, c in pos.get(s2 - s1, []):
                    if c > j and ((m > 1 and j < n - 2) or (m == 1 and c in (j + 1, n - 1)) or (j == n - 2 and r in (0, m - 1))):
                        return True
                        
        return False
