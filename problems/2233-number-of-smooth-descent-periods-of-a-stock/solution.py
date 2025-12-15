class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        add = 0
        last = 0
        ans = 0
        for price in prices:
            ans += 1
            if last - price == 1:
                add += 1
                ans += add
            else:
                add = 0
            last = price
        return ans
