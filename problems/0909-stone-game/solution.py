class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dp(left: int, right: int) -> int:
            if left > right:
                return 0
            return max(
                piles[left] - dp(left + 1, right),
                piles[right] - dp(left, right - 1)
            )

        return dp(0, len(piles) - 1) > 0
