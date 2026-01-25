class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        def check(x, tk):
            cnt = 0
            ck = 0
            for i in range(60, -1, -1):
                if (x >> i) & 1:
                    if tk - ck >= 0:
                        cnt += math.comb(i, tk - ck)

                    ck += 1

            if ck == tk:
                cnt += 1

            return cnt

        low, high = 1, 1 << 60
        res = high
        while low <= high:
            mid = (low + high) // 2
            if check(mid, k) >= n:
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res

