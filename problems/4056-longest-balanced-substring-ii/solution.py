class Solution:
    def longestBalanced(self, s: str) -> int:
        ans = max((len(list(g)) for _, g in itertools.groupby(s)), default=0)
        for u, v, x in [('a', 'b', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b')]:
            diff, idx_map = 0, {0: -1}
            for i, c in enumerate(s):
                if c == x:
                    diff, idx_map = 0, {0: i}
                else:
                    diff += 1 if c == u else -1
                    if diff in idx_map:
                        ans = max(ans, i - idx_map[diff])
                    else:
                        idx_map[diff] = i

        diff_ab, diff_bc, idx_map = 0, 0, {(0, 0): -1}
        for i, c in enumerate(s):
            if c == 'a':
                diff_ab += 1
            elif c == 'b':
                diff_ab -= 1
                diff_bc += 1
            else:
                diff_bc -= 1

            key = (diff_ab, diff_bc)
            if key in idx_map:
                ans = max(ans, i - idx_map[key])
            else:
                idx_map[key] = i

        return ans
