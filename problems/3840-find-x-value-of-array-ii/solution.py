class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        size = 1 << (n - 1).bit_length() if n > 1 else 1
        t_prod = [1] * (2 * size)
        t_cnt = [[0] * k for _ in range(2 * size)]
        for i, x in enumerate(nums):
            v = x % k
            t_prod[size + i] = v
            t_cnt[size + i][v] = 1
        for i in range(size - 1, 0, -1):
            l, r = 2 * i, 2 * i + 1
            t_prod[i] = (t_prod[l] * t_prod[r]) % k
            t_cnt[i] = t_cnt[l][:]
            pl = t_prod[l]
            for j in range(k):
                if t_cnt[r][j]:
                    t_cnt[i][(pl * j) % k] += t_cnt[r][j]
        ans = []
        for idx, val, start, target in queries:
            p = size + idx
            v = val % k
            t_prod[p] = v
            t_cnt[p] = [0] * k
            t_cnt[p][v] = 1
            p //= 2
            while p > 0:
                l, r = 2 * p, 2 * p + 1
                t_prod[p] = (t_prod[l] * t_prod[r]) % k
                t_cnt[p] = t_cnt[l][:]
                pl = t_prod[l]
                for j in range(k):
                    if t_cnt[r][j]:
                        t_cnt[p][(pl * j) % k] += t_cnt[r][j]
                p //= 2
            left, right = size + start, size + n - 1
            ln, rn = [], []
            while left <= right:
                if left % 2 == 1:
                    ln.append(left)
                    left += 1
                if right % 2 == 0:
                    rn.append(right)
                    right -= 1
                left //= 2
                right //= 2
            c_prod = 1
            c_cnt = [0] * k
            for node in ln + rn[::-1]:
                for j in range(k):
                    if t_cnt[node][j]:
                        c_cnt[(c_prod * j) % k] += t_cnt[node][j]
                c_prod = (c_prod * t_prod[node]) % k
            ans.append(c_cnt[target])
        return ans
