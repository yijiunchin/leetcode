class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        high = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        return bisect_left(
            range(high + 1),
            mountainHeight,
            key=lambda mid: sum((math.isqrt(1 + 8 * (mid // t)) - 1) // 2 for t in workerTimes),
        )
