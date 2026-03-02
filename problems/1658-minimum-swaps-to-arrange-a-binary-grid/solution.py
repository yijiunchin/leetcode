class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeros = [n - 1 - max((j for j, v in enumerate(row) if v), default=-1) for row in grid]
        ans = 0
        for i in range(n):
            target = n - 1 - i
            for j in range(i, n):
                if zeros[j] >= target:
                    ans += j - i
                    zeros.insert(i, zeros.pop(j))
                    break
            else:
                return -1

        return ans
