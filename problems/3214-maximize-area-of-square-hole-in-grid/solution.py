class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: list[int], vBars: list[int]
    ) -> int:
        def get_max_gap(bars: list[int]) -> int:
            bars.sort()
            max_cnt = 1
            curr_cnt = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    curr_cnt += 1
                else:
                    curr_cnt = 1
                max_cnt = max(max_cnt, curr_cnt)
            return max_cnt + 1

        h_gap = get_max_gap(hBars)
        v_gap = get_max_gap(vBars)
        side = min(h_gap, v_gap)

        return side * side

