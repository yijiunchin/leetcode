class Solution:
    def minimumK(self, nums: List[int]) -> int:
        l, r = 1, max(max(nums), len(nums))
        while l <= r:
            mid = (l + r) // 2
            options = sum((x + mid - 1) // mid for x in nums)
            if options <= mid ** 2:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans

