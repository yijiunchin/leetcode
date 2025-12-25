class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans = 0
        happiness.sort(reverse=True)
        for i, n in enumerate(happiness):
            happy = n - i
            if happy > 0: ans += happy
            if happy <= 0 or i + 1 == k:
                return ans

