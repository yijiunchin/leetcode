class Solution:
    def _clean(self, h: list[tuple[int, int]], min_i: int) -> None:
        from heapq import heappop
        while h and h[0][1] < min_i:
            heappop(h)

    def _evict(self, nums: list[int], in_l: list[bool], out: int,
               l_sz: int, r_sz: int, l_sum: int, r_sum: int) -> tuple:
        was_l = in_l[out]
        return (
            l_sz - was_l,
            r_sz - (not was_l),
            l_sum - nums[out] * was_l,
            r_sum - nums[out] * (not was_l)
        )

    def _get_costs(self, nums: list[int], x: int) -> list[int]:
        from heapq import heappush, heappop
        in_l = [False] * len(nums)
        l_h, r_h = [], []
        l_sum = r_sum = l_sz = r_sz = 0
        costs = []
        for i, v in enumerate(nums):
            is_l = True
            if l_h:
                is_l = v <= -l_h[0][0]
            in_l[i] = is_l
            if is_l:
                l_sz += 1
                l_sum += v
                heappush(l_h, (-v, i))
            else:
                r_sz += 1
                r_sum += v
                heappush(r_h, (v, i))
            if i >= x:
                l_sz, r_sz, l_sum, r_sum = self._evict(
                    nums, in_l, i - x, l_sz, r_sz, l_sum, r_sum
                )
            min_i = max(0, i - x + 1)
            while l_sz > r_sz + 1:
                val, idx = heappop(l_h)
                if idx >= min_i:
                    l_sum += val
                    l_sz -= 1
                    heappush(r_h, (-val, idx))
                    in_l[idx] = False
                    r_sum -= val
                    r_sz += 1
            while l_sz < r_sz:
                val, idx = heappop(r_h)
                if idx >= min_i:
                    r_sum -= val
                    r_sz -= 1
                    heappush(l_h, (-val, idx))
                    in_l[idx] = True
                    l_sum += val
                    l_sz += 1
            self._clean(l_h, min_i)
            self._clean(r_h, min_i)
            if i >= x - 1:
                costs.append(r_sum - l_sum + (-l_h[0][0]) * (x % 2))
        return costs

    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        costs = self._get_costs(nums, x)
        m = len(costs)
        dp = [0] * (m + x)
        for _ in range(k):
            n_dp = [float('inf')] * (m + x)
            for i in range(m - 1, -1, -1):
                n_dp[i] = min(n_dp[i + 1], costs[i] + dp[i + x])
            dp = n_dp
        return dp[0]
