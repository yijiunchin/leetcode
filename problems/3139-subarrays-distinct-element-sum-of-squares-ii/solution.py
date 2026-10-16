class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        s = [0] * (4 * n)
        z = [0] * (4 * n)

        def u(o: int, l: int, r: int, ql: int, qr: int) -> None:
            if ql <= l and r <= qr:
                s[o] += r - l + 1
                z[o] += 1
                return
            m = (l + r) // 2
            if z[o]:
                s[o * 2] += z[o] * (m - l + 1)
                z[o * 2] += z[o]
                s[o * 2 + 1] += z[o] * (r - m)
                z[o * 2 + 1] += z[o]
                z[o] = 0
            if ql <= m:
                u(o * 2, l, m, ql, qr)
            if qr > m:
                u(o * 2 + 1, m + 1, r, ql, qr)
            s[o] = s[o * 2] + s[o * 2 + 1]

        def q(o: int, l: int, r: int, ql: int, qr: int) -> int:
            if ql <= l and r <= qr:
                return s[o]
            m = (l + r) // 2
            if z[o]:
                s[o * 2] += z[o] * (m - l + 1)
                z[o * 2] += z[o]
                s[o * 2 + 1] += z[o] * (r - m)
                z[o * 2 + 1] += z[o]
                z[o] = 0
            res = 0
            if ql <= m:
                res += q(o * 2, l, m, ql, qr)
            if qr > m:
                res += q(o * 2 + 1, m + 1, r, ql, qr)
            return res

        last = {}
        ans = cur = 0
        for i, x in enumerate(nums):
            p = last.get(x, -1) + 1
            cur += 2 * q(1, 0, n - 1, p, i) + (i - p + 1)
            ans = (ans + cur) % 1_000_000_007
            u(1, 0, n - 1, p, i)
            last[x] = i
        return ans
