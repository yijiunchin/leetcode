class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        a, b, c = float('inf'), float('inf'), 0
        for cost in costs:
            a, b, c = b, c, cost + min(c + 1, b + 4, a + 9)
        return c
