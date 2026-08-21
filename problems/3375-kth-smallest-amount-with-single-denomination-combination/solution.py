class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        lcms = [
            (math.lcm(*c), 1 if len(c) % 2 else -1)
            for i in range(1, len(coins) + 1)
            for c in combinations(coins, i)
        ]
        left, right = 1, min(coins) * k
        while left < right:
            mid = (left + right) // 2
            if sum(s * (mid // l) for l, s in lcms) >= k:
                right = mid
            else:
                left = mid + 1
        return left
