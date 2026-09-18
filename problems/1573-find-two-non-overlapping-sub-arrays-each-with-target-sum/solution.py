class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        dp = [float('inf')] * n
        ans = min_len = float('inf')
        left = window_sum = 0
        
        for right, val in enumerate(arr):
            window_sum += val
            while window_sum > target:
                window_sum -= arr[left]
                left += 1
                
            if window_sum == target:
                curr = right - left + 1
                if left > 0:
                    ans = min(ans, curr + dp[left - 1])
                min_len = min(min_len, curr)
                
            dp[right] = min_len
            
        return ans if ans != float('inf') else -1
