class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid[0])
        flat = [val for row in grid for val in row]
        k %= len(flat)
        res = flat[-k:] + flat[:-k]
        return [res[i : i + n] for i in range(0, len(res), n)]
