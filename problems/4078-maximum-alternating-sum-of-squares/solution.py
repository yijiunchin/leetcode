class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums_len = len(nums)
        positive = nums_len // 2 if nums_len % 2 == 0 else nums_len // 2 + 1
        nums.sort(reverse=True, key=abs)
        ans = 0

        while nums:
            num = nums.pop(0)
            if positive:
                ans += num * num
                positive -= 1
            else:
                ans -= num * num

        return ans

