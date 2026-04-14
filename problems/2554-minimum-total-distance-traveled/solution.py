class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        n = len(robot)
        dp = [0] + [float('inf')] * n
        
        for pos, limit in factory:
            for i in range(n, 0, -1):
                cost = 0
                for k in range(1, min(i, limit) + 1):
                    cost += abs(robot[i - k] - pos)
                    if dp[i - k] + cost < dp[i]:
                        dp[i] = dp[i - k] + cost
                        
        return dp[n]
