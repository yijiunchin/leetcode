class Solution:
    def canAliceWin(self, n: int) -> bool:
        pick = 10
        while n >= pick:
            n -= pick
            pick -= 1
        return (10 - pick) % 2 == 1
