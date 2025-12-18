class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        original_profit = sum(p * s for p, s in zip(prices, strategy))
        prefix_p = [0] * (n + 1)
        prefix_ps = [0] * (n + 1)

        for i in range(n):
            prefix_p[i + 1] = prefix_p[i] + prices[i]
            prefix_ps[i + 1] = prefix_ps[i] + (prices[i] * strategy[i])

        max_delta = 0
        half_k = k // 2

        for i in range(n - k + 1):
            old_segment_profit = prefix_ps[i + k] - prefix_ps[i]
            new_segment_profit = (
                prefix_p[i + k] - prefix_p[i + half_k]
            )
            current_delta = new_segment_profit - old_segment_profit
            if current_delta > max_delta:
                max_delta = current_delta

        return original_profit + max_delta
