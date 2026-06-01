class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        buy_num = total = 0
        for n in sorted(cost, reverse=True):
            if buy_num == 2:
                buy_num = 0
                continue

            total += n
            buy_num += 1

        return total
