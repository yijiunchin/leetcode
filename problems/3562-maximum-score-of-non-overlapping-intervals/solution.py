class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        arr = sorted((x[1], x[0], x[2], i) for i, x in enumerate(intervals))
        ends = [x[0] for x in arr]
        dp = [[(0, ())] * 5 for _ in range(len(arr) + 1)]
        for i in range(1, len(arr) + 1):
            r, l, w, idx = arr[i - 1]
            p = bisect.bisect_left(ends, l)
            for k in range(1, 5):
                w1, s1 = dp[i - 1][k]
                w2_p, s2_p = dp[p][k - 1]
                w2 = w2_p + w
                if w2 > w1:
                    dp[i][k] = (w2, tuple(sorted(s2_p + (idx,))))
                elif w2 == w1:
                    s2 = tuple(sorted(s2_p + (idx,)))
                    dp[i][k] = (w2, s2) if s2 < s1 else (w1, s1)
                else:
                    dp[i][k] = (w1, s1)
        return list(dp[-1][4][1])
