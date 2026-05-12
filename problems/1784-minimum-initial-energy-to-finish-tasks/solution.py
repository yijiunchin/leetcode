class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        ans = 0
        for a, m in sorted(tasks, key=lambda x: x[1] - x[0]):
            ans = max(ans + a, m)
        return ans
