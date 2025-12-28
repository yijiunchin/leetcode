class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        cost1 = min(cost1, costBoth)
        cost2 = min(cost2, costBoth)
        costBoth = min(costBoth, cost1 + cost2)
        basic_need = min(need1, need2)
        return costBoth * basic_need + cost1 * (need1 - basic_need) + cost2 * (need2 - basic_need)

