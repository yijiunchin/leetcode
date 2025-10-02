class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        max_drunk = empty_bottles = 0
        while numBottles != 0 or empty_bottles >= numExchange:
            if empty_bottles >= numExchange:
                empty_bottles -= numExchange
                numBottles += 1
                numExchange += 1
            elif empty_bottles < numExchange:
                empty_bottles += numBottles
                max_drunk += numBottles
                numBottles = 0
        return max_drunk

