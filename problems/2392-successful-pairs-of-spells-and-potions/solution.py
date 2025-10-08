class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        ans = []

        for spell in spells:
            left, right = 0, m

            if spell >= success:
                ans.append(m)
                continue

            while left != right:
                mid = (left + right) // 2
                if spell * potions[mid] < success:
                    left = mid + 1
                else:
                    right = mid

            ans.append(m - left)

        return ans

