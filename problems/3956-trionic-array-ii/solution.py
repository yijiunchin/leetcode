class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        dp_up = dp_down = dp_up2 = ans = -float('inf')
        for i in range(1, n):
            current = nums[i]
            previous = nums[i - 1]
            new_dp_up = new_dp_down = new_dp_up2 = -float('inf')
            if current > previous:
                new_dp_up = max(dp_up, previous) + current
                new_dp_up2 = max(dp_up2, dp_down) + current
            elif current < previous:
                new_dp_down = max(dp_down, dp_up) + current

            dp_up = new_dp_up
            dp_down = new_dp_down
            dp_up2 = new_dp_up2
            ans = max(ans, dp_up2)

        return int(ans)
