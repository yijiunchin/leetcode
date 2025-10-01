class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        max_bottles = empty_bottles = numBottles
        while empty_bottles / numExchange >= 1:
            max_bottles += int(empty_bottles / numExchange)
            empty_bottles = int(empty_bottles / numExchange) + empty_bottles % numExchange
        return max_bottles

