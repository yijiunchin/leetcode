class Solution:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        nums_len = len(nums)
        pre = [0] * (nums_len + 1)
        for i in range(nums_len):
            pre[i + 1] = pre[i] + nums[i]

        dp = [pre[i] * pre[i] for i in range(nums_len + 1)]

        for _ in range(2, k + 1):
            new_dp = [0] * (nums_len + 1)

            def compute(l, r, option_l, option_r):
                if l > r:
                    return

                mid = (l + r) // 2
                best_cost = float('inf')
                best_p = -1
                for p in range(option_l,  min(mid, option_r) + 1):
                    s = pre[mid] - pre[p]
                    c = dp[p] + s ** 2
                    if c < best_cost:
                        best_cost = c
                        best_p = p

                new_dp[mid] = best_cost
                compute(l, mid - 1, option_l, best_p)
                compute(mid + 1, r, best_p, option_r)

            compute(1, nums_len, 0, nums_len - 1)
            dp = new_dp

        return (dp[nums_len] + pre[nums_len]) // 2

