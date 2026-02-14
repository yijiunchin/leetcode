class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        level = [poured]
        for _ in range(query_row):
            overflow = [max((x - 1) / 2, 0) for x in level]
            level = [sum(pair) for pair in zip([0] + overflow, overflow + [0])]
        return min(1, level[query_glass])
