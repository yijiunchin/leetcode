class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len == 1:
            return 1

        ans = 1
        up1 = [1, 1]
        down1 = [1, 1]
        up2 = [1, 1]
        down2 = [1, 1]
        for i in range(1 , nums_len):
            up = [1, 1]
            down = [1, 1]
            if nums[i] > nums[i - 1]:
                up[0] = down1[0] + 1
            elif nums[i] < nums[i - 1]:
                down[0] = up1[0] + 1

            if nums[i] > nums[i - 1]:
                up[1] = max(up[1], down1[1] + 1)
            elif nums[i] < nums[i - 1]:
                down[1] = max(down[1], up1[1] + 1)

            if i >= 2:
                if nums[i] > nums[i - 2]:
                    up[1] = max(up[1], down2[0] + 1)
                elif nums[i] < nums[i - 2]:
                    down[1] = max(down[1], up2[0] + 1)

            ans = max(ans, up[0], down[0], up[1], down[1])
            up2 = list(up1)
            down2 = list(down1)
            up1 = list(up)
            down1 = list(down)

        return ans

